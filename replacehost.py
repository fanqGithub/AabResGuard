import os
import re

# API映射字符串
api_mapping = """
/client/user-profile/update/userInfo | /api/user/info/update | 用户资料更新
/client/user-profile/update/userRegInfo | /api/user/info/update_reg | 注册后修改资料
/client/user-profile/get/userInfo | /api/user/info/get | 查询用户资料
/client/user-profile/get/statusInfo | /api/user/info/status | 查询用户资料完善情况
/client/user-profile/get/levelDetailInfo | /api/user/info/levelDetail | 查询用户等级详情
/client/user-profile/get/wealthLevelInfo | /api/user/info/wealthLevel | 查询用户财富等级(真实)
/client/user-profile/add/album | /api/album/add | 新增相册
/client/user-profile/get/album | /api/album/get | 查询相册
/client/user-profile/del/album | /api/album/del |  删除相册
/client/user-profile/update/albumLocation | /api/album/update_post | 更新相册位置
/client/user-profile/v1/get/user_resource  | /api/resource/v1/query_user_resource | 我的装扮
/client/user-profile/v1/use/user_resource  | /api/resource/v1/use_user_resource | 佩戴
/client/user-profile/v1/check/blackTarget | /api/relation/v1/check_black_target | 检查目标用户拉黑
/client/user-profile/v1/get/userBlackList | /api/relation/v1/user_black_List | 我拉黑的用户列表
/client/user-profile/v1/set/userBlack | /api/relation/v1/user_set_black | 拉黑 or  取消拉黑
/client/user-profile/v1/follow/user | /api/relation/v1/user_follow | 关注 or 取消关注
/client/user-profile/v1/get/userRelationShow | /api/relation/v1/user_relation_show | 个人资料用户关系展示
/client/user-profile/v1/get/userCount | /api/relation/v1/user_count | 个人用户关系数聚合
/client/user-profile/v1/get/userList | /api/relation/v1/user_list | 用户关系列表
/client/user-profile/v1/update/seeMe | /api/relation/v1/update_see_me | 更新谁看过我
/client/user-profile/currencyUser/check/showEnter | /api/currencyUser/showEnter | 是否展示币商入口
/client/user-profile/currencyUser/get/list | /api/currencyUser/list | 币商列表
/client/user-profile/currencyUser/check/transEnter | /api/currencyUser/transEnter | 是否转账支付入口
"""

api_replacements = {}
for line in api_mapping.strip().split('\n'):
    parts = line.split(" | ")
    if len(parts) == 3:
        new_path, old_path = parts[0].strip(), parts[1].strip()
        api_replacements[re.escape(old_path)] = new_path

# 递归遍历目录并替换文件中的 API 路径
def replace_api_paths(directory, script_name):
    replaced_apis = {}  # 用于记录被替换的API路径

    for root, dirs, files in os.walk(directory):
        for file in files:
            if file == script_name:  # 跳过当前脚本文件
                continue
            file_path = os.path.join(root, file)
            try:
                with open(file_path, 'r+', encoding='utf-8') as f:
                    content = f.read()

                    # 检查并替换每个 API 路径
                    content_modified = False
                    for old_path, new_path in api_replacements.items():
                        count = content.count(old_path)
                        if count > 0:
                            content = content.replace(old_path, new_path)
                            content_modified = True
                            if old_path not in replaced_apis:
                                replaced_apis[old_path] = 0
                            replaced_apis[old_path] += count

                    # 如果有替换发生，写回文件
                    if content_modified:
                        print(f"Replaced APIs in {file_path}:")
                        for old_path, count in replaced_apis.items():
                            print(f"  - {old_path} -> {api_replacements[old_path]} ({count} times)")
                        f.seek(0)
                        f.write(content)
                        f.truncate()  # 裁剪文件，防止原始内容之后的内容残留
            except Exception as e:
                print(f"Error processing file {file_path}: {e}")

# 调用函数，传入项目根目录和脚本文件名
project_root_directory = os.getcwd()  # 修改为你的项目根目录路径
# 你的脚本文件名，根据实际情况修改
script_filename = os.path.basename('replacehost.py')
replace_api_paths(project_root_directory, script_filename)