from PIL import Image, ImageDraw, ImageFont
from f1Class import F1

class createImages():
    def __init__(self):
        self.font = 'F1Twitter\Roboto-Regular.ttf'
        self.twitter = '@f1informacoes'
        self.f1 = F1()
        
    def createQualifyImg(self):
        blank_image = Image.new('RGB', (1080, 1080), 'white')
        font = ImageFont.truetype(self.font, 35)
        img_draw = ImageDraw.Draw(blank_image)
        img_draw.rectangle([0, 75, 1080, 1080], fill='gray')
        img_draw.text((820, 1020), self.twitter, fill='white', font=font)
        img_draw.text((10, 20), f'Resultado do Qualify em {self.f1.lastGP()}', fill='black', font=font)
        img_draw.text((10, 90), self.f1.qualifyResult(), fill='black', font=font)
        blank_image.save('qualifyImage.jpg')
        
    def createRaceResultImg(self):
        blank_image = Image.new('RGB', (1080, 1080), 'white')
        font = ImageFont.truetype(self.font, 35)
        img_draw = ImageDraw.Draw(blank_image)
        img_draw.rectangle([0, 75, 1080, 1080], fill='gray')
        img_draw.text((820, 1020), self.twitter, fill='white', font=font)
        img_draw.text((10, 20), f'Resultado da Corrida em {self.f1.lastGP()}', fill='black', font=font)
        img_draw.text((10,90), self.f1.raceResult(), fill='black', font=font)
        blank_image.save('raceResult.jpg')
        
        
    def createConstructorResultImg(self):
        blank_image = Image.new('RGB', (1080, 550), 'white')
        font = ImageFont.truetype(self.font, 35)
        img_draw = ImageDraw.Draw(blank_image)
        img_draw.rectangle([0, 75, 1080, 550], fill='gray')
        img_draw.text((820, 500), self.twitter, fill='white', font=font)
        img_draw.text((7, 20), f'Resultado do campeonato de construtores em {self.f1.lastGP()}', fill='black', font=font)
        img_draw.text((10,90), self.f1.constructorResults(), fill='black', font=font)
        blank_image.save('constructorResult.jpg')
        print('Imagem criada com sucesso!')
        
