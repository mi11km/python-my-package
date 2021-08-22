import json
import subprocess

""" lambda関数の詳細情報をjson化しようとしたスクリプト """

cmd = ["aws", "lambda", "--profile", "jx", "list-functions"]
res = subprocess.check_output(cmd)
functions = json.loads(res.decode("utf-8"))["Functions"]

function_names = []

with open("env.json", "w") as f:
    data = {}
    for func in functions:
        name = func["FunctionName"]
        function_names.append(name)
        if func.get("Environment"):
            if func.get("Environment").get("Variables"):
                data[name] = func["Environment"]["Variables"]
    f.write(str(data))


# code_src_data = {}
for name in function_names:
    cmd = ["aws", "lambda", "--profile", "jx", "get-function", "--function-name", name]
    res = subprocess.check_output(cmd)
    function_detail = json.loads(res.decode("utf-8"))
    if function_detail.get("Code"):
        download_cmd = ["curl", "-o", f"{name}.zip", function_detail["Code"]["Location"]]
        subprocess.call(download_cmd)
        unzip_cmd = []
        # code_info = function_detail["Code"]
        # code_src_data[name] = code_info

# with open("src.json", "w") as f:
#     f.write(str(code_src_data))

