from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from pprint import pprint
from .models import Respuesta

def modelo(id):
    model = SentenceTransformer('paraphrase-multilingual-MiniLM-L12-v2')
    if(id==1):
        respuesta = Respuesta.objects.filter(pregunta_id=id).last()
        preg1=respuesta.respuesta
        respuestas1=['nada',
             'algo',
             'bastante',
             'muy']
        embeddings1=model.encode(respuestas1)
        input1=model.encode(preg1)

        largo1= len(embeddings1)
        r11=cosine_similarity(embeddings1[0].reshape(1,-1), input1.reshape(1,-1))
        r12=cosine_similarity(embeddings1[1].reshape(1,-1), input1.reshape(1,-1))
        r13=cosine_similarity(embeddings1[2].reshape(1,-1), input1.reshape(1,-1))
        r14=cosine_similarity(embeddings1[3].reshape(1,-1), input1.reshape(1,-1))

        lista_respuestas1=[r11,r12,r13,r14]
        


        aux=lista_respuestas1[0]
        punt1=4
        for i in range(len(lista_respuestas1)) :
         if (lista_respuestas1[i]>aux):
          aux=lista_respuestas1[i]
          punt1= 4 - i
        respuesta.puntuacion=punt1
        respuesta.save()
        return 

    if(id==2):
        respuesta = Respuesta.objects.filter(pregunta_id=id).last()
        preg2=respuesta.respuesta
        respuestas2=['nada',
             'algo',
             'bastante',
             'muy']
        embeddings2=model.encode(respuestas2)
        input2=model.encode(preg2)

        largo2= len(embeddings2)
        r21=cosine_similarity(embeddings2[0].reshape(1,-1), input2.reshape(1,-1))
        r22=cosine_similarity(embeddings2[1].reshape(1,-1), input2.reshape(1,-1))
        r23=cosine_similarity(embeddings2[2].reshape(1,-1), input2.reshape(1,-1))
        r24=cosine_similarity(embeddings2[3].reshape(1,-1), input2.reshape(1,-1))

        lista_respuestas2=[r21,r22,r23,r24]
        


        aux=lista_respuestas2[0]
        punt2=4
        for i in range(len(lista_respuestas2)) :
         if (lista_respuestas2[i]>aux):
          aux=lista_respuestas2[i]
          punt2= 4 - i
        
        respuesta.puntuacion=punt2
        respuesta.save()
        return 
    
    if(id==3):
        respuesta = Respuesta.objects.filter(pregunta_id=id).last()
        preg3=respuesta.respuesta
        respuestas3=['nada',
             'algo',
             'bastante',
             'muy']
        embeddings3=model.encode(respuestas3)
        input3=model.encode(preg3)

        largo3= len(embeddings3)
        r31=cosine_similarity(embeddings3[0].reshape(1,-1), input3.reshape(1,-1))
        r32=cosine_similarity(embeddings3[1].reshape(1,-1), input3.reshape(1,-1))
        r33=cosine_similarity(embeddings3[2].reshape(1,-1), input3.reshape(1,-1))
        r34=cosine_similarity(embeddings3[3].reshape(1,-1), input3.reshape(1,-1))

        lista_respuestas3=[r31,r32,r33,r34]
        


        aux=lista_respuestas3[0]
        punt3=1
        for i in range(len(lista_respuestas3)) :
         if (lista_respuestas3[i]>aux):
          aux=lista_respuestas3[i] 
          punt3= i + 1
        respuesta.puntuacion=punt3
        respuesta.save()
        return 


    if(id==4):
        respuesta = Respuesta.objects.filter(pregunta_id=id).last()
        preg4 = respuesta.respuesta
        respuestas4 = ['nada', 'algo', 'bastante', 'muy']
        embeddings4 = model.encode(respuestas4)
        input4 = model.encode(preg4)

        r41 = cosine_similarity(embeddings4[0].reshape(1, -1), input4.reshape(1, -1))
        r42 = cosine_similarity(embeddings4[1].reshape(1, -1), input4.reshape(1, -1))
        r43 = cosine_similarity(embeddings4[2].reshape(1, -1), input4.reshape(1, -1))
        r44 = cosine_similarity(embeddings4[3].reshape(1, -1), input4.reshape(1, -1))

        lista_respuestas4 = [r41, r42, r43, r44]

        aux = lista_respuestas4[0]
        punt4 = 1
        for i in range(len(lista_respuestas4)):
          if lista_respuestas4[i] > aux:
            aux = lista_respuestas4[i]
            punt4 = i + 1
        respuesta.puntuacion = punt4
        respuesta.save()
        return
    
    if(id==5):
        respuesta = Respuesta.objects.filter(pregunta_id=id).last()
        preg5=respuesta.respuesta
        respuestas5=['nada',
                     'algo',
                     'bastante',
                     'muy']
        embeddings5=model.encode(respuestas5)
        input5=model.encode(preg5)

        largo5= len(embeddings5)
        r51=cosine_similarity(embeddings5[0].reshape(1,-1), input5.reshape(1,-1))
        r52=cosine_similarity(embeddings5[1].reshape(1,-1), input5.reshape(1,-1))
        r53=cosine_similarity(embeddings5[2].reshape(1,-1), input5.reshape(1,-1))
        r54=cosine_similarity(embeddings5[3].reshape(1,-1), input5.reshape(1,-1))

        lista_respuestas5=[r51, r52, r53, r54]

        aux=lista_respuestas5[0]
        punt5=4
        for i in range(len(lista_respuestas5)):
          if (lista_respuestas5[i] > aux):
            aux = lista_respuestas5[i]
            punt5 = 4- i
        respuesta.puntuacion = punt5
        respuesta.save()
        return
    

    if(id==6):
        respuesta = Respuesta.objects.filter(pregunta_id=id).last()
        preg6=respuesta.respuesta
        respuestas6=['nada',
                     'algo',
                     'bastante',
                     'muy']
        embeddings6=model.encode(respuestas6)
        input6=model.encode(preg6)

        largo6= len(embeddings6)
        r61=cosine_similarity(embeddings6[0].reshape(1,-1), input6.reshape(1,-1))
        r62=cosine_similarity(embeddings6[1].reshape(1,-1), input6.reshape(1,-1))
        r63=cosine_similarity(embeddings6[2].reshape(1,-1), input6.reshape(1,-1))
        r64=cosine_similarity(embeddings6[3].reshape(1,-1), input6.reshape(1,-1))

        lista_respuestas6=[r61, r62, r63, r64]

        aux=lista_respuestas6[0]
        punt6=1
        for i in range(len(lista_respuestas6)):
          if (lista_respuestas6[i] > aux):
            aux = lista_respuestas6[i]
            punt6 = i + 1
        respuesta.puntuacion = punt6
        respuesta.save()
        return

    if(id == 7):
        respuesta = Respuesta.objects.filter(pregunta_id=id).last()
        preg7 = respuesta.respuesta
        respuestas7 = ['nada', 'algo', 'bastante', 'muy']
        embeddings7 = model.encode(respuestas7)
        input7 = model.encode(preg7)

        r71 = cosine_similarity(embeddings7[0].reshape(1, -1), input7.reshape(1, -1))
        r72 = cosine_similarity(embeddings7[1].reshape(1, -1), input7.reshape(1, -1))
        r73 = cosine_similarity(embeddings7[2].reshape(1, -1), input7.reshape(1, -1))
        r74 = cosine_similarity(embeddings7[3].reshape(1, -1), input7.reshape(1, -1))

        lista_respuestas7 = [r71, r72, r73, r74]

        aux = lista_respuestas7[0]
        punt7 = 1
        for i in range(len(lista_respuestas7)):
            if lista_respuestas7[i] > aux:
                aux = lista_respuestas7[i]
                punt7 = i + 1 

        respuesta.puntuacion = punt7
        respuesta.save()
        return
    

    if(id == 8):
        respuesta = Respuesta.objects.filter(pregunta_id=id).last()
        preg8 = respuesta.respuesta
        respuestas8 = ['nada', 'algo', 'bastante', 'muy']
        embeddings8 = model.encode(respuestas8)
        input8 = model.encode(preg8)

        r81 = cosine_similarity(embeddings8[0].reshape(1, -1), input8.reshape(1, -1))
        r82 = cosine_similarity(embeddings8[1].reshape(1, -1), input8.reshape(1, -1))
        r83 = cosine_similarity(embeddings8[2].reshape(1, -1), input8.reshape(1, -1))
        r84 = cosine_similarity(embeddings8[3].reshape(1, -1), input8.reshape(1, -1))

        lista_respuestas8 = [r81, r82, r83, r84]

        aux = lista_respuestas8[0]
        punt8 = 4
        for i in range(len(lista_respuestas8)):
            if lista_respuestas8[i] > aux:
                aux = lista_respuestas8[i]
                punt8 =4 - i

        respuesta.puntuacion = punt8
        respuesta.save()
        return
    
    if (id == 9):
        respuesta = Respuesta.objects.filter(pregunta_id=id).last()
        preg9 = respuesta.respuesta
        respuestas9 = ['nada', 'algo', 'bastante', 'muy']
        embeddings9 = model.encode(respuestas9)
        input9 = model.encode(preg9)

        r91 = cosine_similarity(embeddings9[0].reshape(1, -1), input9.reshape(1, -1))
        r92 = cosine_similarity(embeddings9[1].reshape(1, -1), input9.reshape(1, -1))
        r93 = cosine_similarity(embeddings9[2].reshape(1, -1), input9.reshape(1, -1))
        r94 = cosine_similarity(embeddings9[3].reshape(1, -1), input9.reshape(1, -1))

        lista_respuestas9 = [r91, r92, r93, r94]

        aux = lista_respuestas9[0]
        punt9 = 1
        for i in range(len(lista_respuestas9)):
            if lista_respuestas9[i] > aux:
                aux = lista_respuestas9[i]
                punt9 = i + 1

        respuesta.puntuacion = punt9
        respuesta.save()
        return      
    
    if (id == 10):
        respuesta = Respuesta.objects.filter(pregunta_id=id).last()
        preg10 = respuesta.respuesta
        respuestas10 = ['nada', 'algo', 'bastante', 'muy']
        embeddings10 = model.encode(respuestas10)
        input10 = model.encode(preg10)

        r101 = cosine_similarity(embeddings10[0].reshape(1, -1), input10.reshape(1, -1))
        r102 = cosine_similarity(embeddings10[1].reshape(1, -1), input10.reshape(1, -1))
        r103 = cosine_similarity(embeddings10[2].reshape(1, -1), input10.reshape(1, -1))
        r104 = cosine_similarity(embeddings10[3].reshape(1, -1), input10.reshape(1, -1))

        lista_respuestas10 = [r101, r102, r103, r104]

        aux = lista_respuestas10[0]
        punt10 = 4
        for i in range(len(lista_respuestas10)):
            if lista_respuestas10[i] > aux:
                aux = lista_respuestas10[i]
                punt10 =4 - i

        respuesta.puntuacion = punt10
        respuesta.save()
        return
    
    if (id == 11):
        respuesta = Respuesta.objects.filter(pregunta_id=id).last()
        preg11 = respuesta.respuesta
        respuestas11 = ['nada', 'algo', 'bastante', 'mucha']
        embeddings11 = model.encode(respuestas11)
        input11 = model.encode(preg11)

        r111 = cosine_similarity(embeddings11[0].reshape(1, -1), input11.reshape(1, -1))
        r112 = cosine_similarity(embeddings11[1].reshape(1, -1), input11.reshape(1, -1))
        r113 = cosine_similarity(embeddings11[2].reshape(1, -1), input11.reshape(1, -1))
        r114 = cosine_similarity(embeddings11[3].reshape(1, -1), input11.reshape(1, -1))

        lista_respuestas11 = [r111, r112, r113, r114]

        aux = lista_respuestas11[0]
        punt11 = 4
        for i in range(len(lista_respuestas11)):
            if lista_respuestas11[i] > aux:
                aux = lista_respuestas11[i]
                punt11 = 4 - i

        respuesta.puntuacion = punt11
        respuesta.save()
        return
    
    if (id == 12):
        respuesta = Respuesta.objects.filter(pregunta_id=id).last()
        preg12 = respuesta.respuesta
        respuestas12 = ['nada', 'algo', 'bastante', 'muy']
        embeddings12 = model.encode(respuestas12)
        input12 = model.encode(preg12)

        r121 = cosine_similarity(embeddings12[0].reshape(1, -1), input12.reshape(1, -1))
        r122 = cosine_similarity(embeddings12[1].reshape(1, -1), input12.reshape(1, -1))
        r123 = cosine_similarity(embeddings12[2].reshape(1, -1), input12.reshape(1, -1))
        r124 = cosine_similarity(embeddings12[3].reshape(1, -1), input12.reshape(1, -1))

        lista_respuestas12 = [r121, r122, r123, r124]

        aux = lista_respuestas12[0]
        punt12 = 1
        for i in range(len(lista_respuestas12)):
            if lista_respuestas12[i] > aux:
                aux = lista_respuestas12[i]
                punt12 = i + 1

        respuesta.puntuacion = punt12
        respuesta.save()
        return
    
    if (id == 13):
        respuesta = Respuesta.objects.filter(pregunta_id=id).last()
        preg13 = respuesta.respuesta
        respuestas13 = ['nada', 'algo', 'bastante', 'muy']
        embeddings13 = model.encode(respuestas13)
        input13 = model.encode(preg13)

        r131 = cosine_similarity(embeddings13[0].reshape(1, -1), input13.reshape(1, -1))
        r132 = cosine_similarity(embeddings13[1].reshape(1, -1), input13.reshape(1, -1))
        r133 = cosine_similarity(embeddings13[2].reshape(1, -1), input13.reshape(1, -1))
        r134 = cosine_similarity(embeddings13[3].reshape(1, -1), input13.reshape(1, -1))

        lista_respuestas13 = [r131, r132, r133, r134]

        aux = lista_respuestas13[0]
        punt13 = 1
        for i in range(len(lista_respuestas13)):
            if lista_respuestas13[i] > aux:
                aux = lista_respuestas13[i]
                punt13 = i + 1 

        respuesta.puntuacion = punt13
        respuesta.save()
        return
    
    if (id == 14):
        respuesta = Respuesta.objects.filter(pregunta_id=id).last()
        preg14 = respuesta.respuesta
        respuestas14 = ['nada', 'algo', 'bastante', 'muy']
        embeddings14 = model.encode(respuestas14)
        input14 = model.encode(preg14)

        r141 = cosine_similarity(embeddings14[0].reshape(1, -1), input14.reshape(1, -1))
        r142 = cosine_similarity(embeddings14[1].reshape(1, -1), input14.reshape(1, -1))
        r143 = cosine_similarity(embeddings14[2].reshape(1, -1), input14.reshape(1, -1))
        r144 = cosine_similarity(embeddings14[3].reshape(1, -1), input14.reshape(1, -1))

        lista_respuestas14 = [r141, r142, r143, r144]

        aux = lista_respuestas14[0]
        punt14 = 1
        for i in range(len(lista_respuestas14)):
            if lista_respuestas14[i] > aux:
                aux = lista_respuestas14[i]
                punt14 = i + 1

        respuesta.puntuacion = punt14
        respuesta.save()
        return
    
    if (id == 15):
        respuesta = Respuesta.objects.filter(pregunta_id=id).last()
        preg15 = respuesta.respuesta
        respuestas15 = ['nada', 'algo', 'bastante', 'muy']
        embeddings15 = model.encode(respuestas15)
        input15 = model.encode(preg15)

        r151 = cosine_similarity(embeddings15[0].reshape(1, -1), input15.reshape(1, -1))
        r152 = cosine_similarity(embeddings15[1].reshape(1, -1), input15.reshape(1, -1))
        r153 = cosine_similarity(embeddings15[2].reshape(1, -1), input15.reshape(1, -1))
        r154 = cosine_similarity(embeddings15[3].reshape(1, -1), input15.reshape(1, -1))

        lista_respuestas15 = [r151, r152, r153, r154]

        aux = lista_respuestas15[0]
        punt15 = 4
        for i in range(len(lista_respuestas15)):
            if lista_respuestas15[i] > aux:
                aux = lista_respuestas15[i]
                punt15 = 4 - i

        respuesta.puntuacion = punt15
        respuesta.save()
        return
    
    if (id == 16):
        respuesta = Respuesta.objects.filter(pregunta_id=id).last()
        preg16 = respuesta.respuesta
        respuestas16 = ['nada', 'algo', 'bastante', 'muy']
        embeddings16 = model.encode(respuestas16)
        input16 = model.encode(preg16)

        r161 = cosine_similarity(embeddings16[0].reshape(1, -1), input16.reshape(1, -1))
        r162 = cosine_similarity(embeddings16[1].reshape(1, -1), input16.reshape(1, -1))
        r163 = cosine_similarity(embeddings16[2].reshape(1, -1), input16.reshape(1, -1))
        r164 = cosine_similarity(embeddings16[3].reshape(1, -1), input16.reshape(1, -1))

        lista_respuestas16 = [r161, r162, r163, r164]

        aux = lista_respuestas16[0]
        punt16 = 4
        for i in range(len(lista_respuestas16)):
            if lista_respuestas16[i] > aux:
                aux = lista_respuestas16[i]
                punt16 = 4 - i

        respuesta.puntuacion = punt16
        respuesta.save()
        return
    
    if (id == 17):
        respuesta = Respuesta.objects.filter(pregunta_id=id).last()
        preg17 = respuesta.respuesta
        respuestas17 = ['nada', 'algo', 'bastante', 'muy']
        embeddings17 = model.encode(respuestas17)
        input17 = model.encode(preg17)

        r171 = cosine_similarity(embeddings17[0].reshape(1, -1), input17.reshape(1, -1))
        r172 = cosine_similarity(embeddings17[1].reshape(1, -1), input17.reshape(1, -1))
        r173 = cosine_similarity(embeddings17[2].reshape(1, -1), input17.reshape(1, -1))
        r174 = cosine_similarity(embeddings17[3].reshape(1, -1), input17.reshape(1, -1))

        lista_respuestas17 = [r171, r172, r173, r174]

        aux = lista_respuestas17[0]
        punt17 = 1
        for i in range(len(lista_respuestas17)):
            if lista_respuestas17[i] > aux:
                aux = lista_respuestas17[i]
                punt17 = i + 1

        respuesta.puntuacion = punt17
        respuesta.save()
        return
    
    if (id == 18):
        respuesta = Respuesta.objects.filter(pregunta_id=id).last()
        preg18 = respuesta.respuesta
        respuestas18 = ['nada', 'algo', 'bastante', 'muy']
        embeddings18 = model.encode(respuestas18)
        input18 = model.encode(preg18)

        r181 = cosine_similarity(embeddings18[0].reshape(1, -1), input18.reshape(1, -1))
        r182 = cosine_similarity(embeddings18[1].reshape(1, -1), input18.reshape(1, -1))
        r183 = cosine_similarity(embeddings18[2].reshape(1, -1), input18.reshape(1, -1))
        r184 = cosine_similarity(embeddings18[3].reshape(1, -1), input18.reshape(1, -1))

        lista_respuestas18 = [r181, r182, r183, r184]

        aux = lista_respuestas18[0]
        punt18 = 1
        for i in range(len(lista_respuestas18)):
            if lista_respuestas18[i] > aux:
                aux = lista_respuestas18[i]
                punt18 = i + 1 

        respuesta.puntuacion = punt18
        respuesta.save()
        return
    
    if (id == 19):
        respuesta = Respuesta.objects.filter(pregunta_id=id).last()
        preg19 = respuesta.respuesta
        respuestas19 = ['nada', 'algo', 'bastante', 'muy']
        embeddings19 = model.encode(respuestas19)
        input19 = model.encode(preg19)

        r191 = cosine_similarity(embeddings19[0].reshape(1, -1), input19.reshape(1, -1))
        r192 = cosine_similarity(embeddings19[1].reshape(1, -1), input19.reshape(1, -1))
        r193 = cosine_similarity(embeddings19[2].reshape(1, -1), input19.reshape(1, -1))
        r194 = cosine_similarity(embeddings19[3].reshape(1, -1), input19.reshape(1, -1))

        lista_respuestas19 = [r191, r192, r193, r194]

        aux = lista_respuestas19[0]
        punt19 = 4
        for i in range(len(lista_respuestas19)):
            if lista_respuestas19[i] > aux:
                aux = lista_respuestas19[i]
                punt19 =4 - i

        respuesta.puntuacion = punt19
        respuesta.save()
        return
    
    if (id == 20):
        respuesta = Respuesta.objects.filter(pregunta_id=id).last()
        preg20 = respuesta.respuesta
        respuestas20 = ['nada', 'algo', 'bastante', 'muy']
        embeddings20 = model.encode(respuestas20)
        input20 = model.encode(preg20)

        r201 = cosine_similarity(embeddings20[0].reshape(1, -1), input20.reshape(1, -1))
        r202 = cosine_similarity(embeddings20[1].reshape(1, -1), input20.reshape(1, -1))
        r203 = cosine_similarity(embeddings20[2].reshape(1, -1), input20.reshape(1, -1))
        r204 = cosine_similarity(embeddings20[3].reshape(1, -1), input20.reshape(1, -1))

        lista_respuestas20 = [r201, r202, r203, r204]

        aux = lista_respuestas20[0]
        punt20 = 4
        for i in range(len(lista_respuestas20)):
            if lista_respuestas20[i] > aux:
                aux = lista_respuestas20[i]
                punt20 = 4 - i

        respuesta.puntuacion = punt20
        respuesta.save()
        return
