import cv2
import os
from PIL import Image
def main(nome):

 
    camera_port = (0,cv2.CAP_DSHOW) 
  
    nFrames = 30
  
    camera = cv2.VideoCapture(0,cv2.CAP_DSHOW)
     
    file = "C:/sistema_loja-main/imagens_clientes/"+nome+".png"
         
    print ("Digite <ESC> para sair / <s> para Salvar" )  
     
    emLoop=True
      
    while(emLoop):
     
        retval, img = camera.read()
        cv2.imshow("C:/sistema_loja-main/imagens_clientes/",img)
     
        k = cv2.waitKey(30) & 0xff
     
        if k == 27:
            emLoop=False
            break
        elif k == ord(' '):
            cv2.imwrite(file,img)
            emLoop= False
            carregar_foto(nome)
    camera.release() 
    cv2.destroyAllWindows()
    
    return 0

def carregar_foto(nome):
    diretorio ="C:/sistema_loja-main/imagens_clientes"
    lista_de_arquivo = os.listdir(diretorio)
    if nome+".png" in lista_de_arquivo:
        imagens = Image.open("C:/sistema_loja-main/imagens_clientes/"+nome+".png")
        imagens_2 = imagens.resize((225,225))
        nome_sem_ext = os.path.splitext(nome+".png")[0]
        imagens_2.save(os.path.join("C:/sistema_loja-main/imagens_clientes",nome_sem_ext+".gif"))
        return imagens_2
    else:               
        print("AQUI")
        main(nome)

