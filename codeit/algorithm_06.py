def move_disk(disk_num, start_peg, end_peg):
    print("%d번 원판을 %d번 기둥에서 %d번 기둥으로 이동" % (disk_num, start_peg, end_peg))

def hanoi(num_disks, start_peg, end_peg):
    # 코드를 입력하세요.
    if num_disks==1:
        disk_num=1
        move_disk(disk_num,start_peg,end_peg)
    elif num_disks==2:
      disk_num=1
      end_peg=2
      move_disk(disk_num,start_peg, end_peg)
      
        

# 테스트 코드 (포함하여 제출해주세요)
hanoi(1, 1, 3)