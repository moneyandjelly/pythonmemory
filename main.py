import psutil


def find_process_id(process_name):
    "프로세스 이름으로 PID를 찾습니다."
    for proc in psutil.process_iter(attrs=["pid", "name"]):
        if proc.info["name"].lower() == process_name.lower():
            return proc.info["pid"]
    return None


process_name = "Notepad.exe"
pid = find_process_id(process_name)
if pid is None:
    print(f"{process_name} 프로세스를 찾을 수 없습니다.")
else:
    print(f"{process_name} 프로세스를 찾았습니다")
