from headers import *
from paddle import paddle
from time import sleep
from keys_hit import keys_hit
from ball import ball
from block import block
from bullets import bullets
init()
from board import board

x=58
y=20
lives=3
brd=board(60,70)
new_paddle = paddle()
kb=keys_hit()
bb=ball()
x2=round(bb.getx())
s_t=time.time()
pow_start=0
pow_start_time=0
y2=round(bb.gety())
blk1=[block(3),block(3),block(3),block(3),block(3),block(3),block(3)]
blk2=[block(2),block(2),block(2),block(2),block(2),block(2),block(2)]
blk3=[block(1),block(1),block(1),block(1),block(1),block(1),block(1)]
blkr=block(4)
blk_len=7
level=1
cnt=9
while level<=3:
    
    if bb.getexit()==1 or lives==0:
        os.system('clear')
        print(end="\n\n\n\n\n\n\n\n\n\n\t\t\t")
        print("GAME OVER, WELL PLAYED",end="\n\n\t\t\t")
        print("your score is    ",bb.getscore(),end="\n\n\n\n\n\n")

        break
    if bb.isdead():
        bb.refresh2()
        lives-=1
        x=58
        y=20
        brd.changeurpow()
        pow_start=0
        brd.removeblts()
    brd.refresh()
    if bb.getnoblks()==cnt:
        level+=1
        x=58
        y=20
        pow_start=0
        #brd.removeblts()
        bb.refresh()
        brd.changeurpow()
        pow_start=0
        blk1=[block(3),block(3),block(3),block(3),block(3),block(3),block(3)]
        blk2=[block(2),block(2),block(3),block(2),block(2),block(3),block(2)]
        blk3=[block(1),block(1),block(1),block(1),block(1),block(1),block(1)]
        blkr=block(4)
    if kb.keyhit():
        char=kb.hitkey()
        if(char == 'a'):
            y-=4
            if(y<=0):
                y=0
        if(char == 'd'):
            y+=4
            if(y>=57):
                y=57
        if(char == 'q'):
            break
        if(char == 's'):
            bb.setmove()
        if(char == 'n'):
            level+=1


    brd.addpaddle(new_paddle,x,y,12)
    
    pow_cur_time=time.time()
    if (int(pow_cur_time)-pow_start_time)>6:
        pow_start=0
    if pow_start==1:
        c_time=time.time()
        if int(10*(c_time-s_t))%10==0:
            brd.addbullet(new_paddle)
        brd.bullethit()
    j=25
    if level==2:
        for i in range(2):
            brd.addblock(blk1[i],5+bb.getfall(),j,12,new_paddle)
            j+=25
        j=5
        for i in range(2):
            brd.addblock(blk2[i],11+bb.getfall(),j,12,new_paddle)
            j+=25
        j=25
        for i in range(2):
            brd.addblock(blk3[i],17+bb.getfall(),j,12,new_paddle)
            j+=25
        j=5
        for i in range(2,4):
            brd.addblock(blk1[i],23+bb.getfall(),j,12,new_paddle)
            j+=25
        j=25
        for i in range(2,4):
            brd.addblock(blk2[i],29+bb.getfall(),j,12,new_paddle)
            j+=25
        j=5
        for i in range(2,4):
            brd.addblock(blk3[i],35+bb.getfall(),j,12,new_paddle)
            j+=25
        j=25
        brd.addblock(blkr,41+bb.getfall(),j,12,new_paddle)
    if level==1:
        j=5
        for i in range(4):
            brd.addblock(blk1[i],9+bb.getfall(),j,12,new_paddle)
            j+=13
        j=5
        for i in range(4):
            brd.addblock(blk2[i],5+bb.getfall(),j,12,new_paddle)
            j+=13
        j=5
        for i in range(4):
            brd.addblock(blk3[i],13+bb.getfall(),j,12,new_paddle)
            j+=13
    
    pow_start2=brd.checkpow()
    if pow_start2==1:
        pow_start=1
    if pow_start2==1:
        pow_start_time=int(time.time())
        brd.changeurpow()
    x2=round(bb.getx())
    y2=round(bb.gety())
    new_paddle.checkhit(bb)
    for i in range(4):
        blk1[i].checkhit(bb,x2,y2)
        blk2[i].checkhit(bb,x2,y2)
        blk3[i].checkhit(bb,x2,y2)
        brd.checkhit(bb,blk1[i])
        brd.checkhit(bb,blk2[i])
        brd.checkhit(bb,blk3[i])
    blkr.checkhit(bb,x2,y2)
    brd.checkhit(bb,blkr)
    bb.present()
    brd.getball(bb)
    os.system('clear')
    print("\033[%d;%dH" % (0, 0), end='')
    cur_time=time.time()
    print(Fore.WHITE + Back.BLACK + "\t\t\t\tBrick Breaker",end ="\t\t\t")
    print()
    cur_time=time.time()
    print(Back.BLACK + "Score",bb.getscore(),end ="\t\t")
    print(Back.BLACK+"Level ",level,end="\t")
    print(Back.BLACK+"Lives ",lives,end="\t")
    cur_time=time.time()
    print(Back.BLACK + "Lives Rem:",end ="\t\t")
    cur_time=time.time()
    print(Back.BLACK + "Time elapsed:",int(cur_time -s_t),"sec",end ="\t\t\t")
    print()
    brd.printmarix()
    time.sleep(0.1)

os.system('clear')
print(end="\n\n\n\n\n\n\n\n\n\n\t\t\t")
print("GAME OVER, WELL PLAYED",end="\n\n\t\t\t")
print("your score is    ",bb.getscore(),end="\n\n\n\n\n\n")

