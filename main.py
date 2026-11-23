import json
import random
import pygame

with open("textrpg2.json") as arquivo:
    dados = json.load(arquivo)
    
pygame.init( )
time = random.choice(["sol", "lua", "chuva", "nenhum"])
cores_clima = {
    "sol": (160, 40, 0),
    "lua": (150, 0, 240),
    "chuva": (10, 0, 190),
    "nenhum": (30, 30, 30)
}
tela = pygame.display.set_mode(( 0, 0), pygame.FULLSCREEN)
relogio = pygame.time.Clock( )
tempo_zumbi = 0
tempo_esqueleto = 0
tempo_bandido = 0
tempo_Troll = 0
tempo_Boss = 0

cura = True
rodando = True

vida_player = dados["player"]["vida"] + dados[time]["player"]["vida"]
dano_player = dados["player"]["dano"] + dados[time]["player"]["dano"]
vida_esqueleto = dados["esqueleto"]["vida"] + dados[time] ["esqueleto"]["vida"]
dano_esqueleto = dados["esqueleto"]["dano"] + dados[time] ["esqueleto"] ["dano"]
vida_zumbi = dados["zumbi"]["vida"] + dados[time]["zumbi"]["vida"]
dano_zumbi = dados["zumbi"]["dano"] + dados[time]["zumbi"]["dano"]
vida_bandido = dados["bandido"]["vida"] + dados[time]["bandido"]["vida"]
dano_bandido = dados["bandido"]["dano"] + dados[time]["bandido"]["dano"]
vida_Troll = dados["Troll"]["vida"] + dados[time]["Troll"]["vida"]
dano_Troll = dados["Troll"]["dano"] + dados[time]["Troll"]["dano"]
vida_Boss = dados["Boss"]["vida"] + dados[time]["Boss"]["vida"]
dano_Boss = dados["Boss"]["dano"] + dados[time]["Boss"]["dano"]


player = pygame.Rect(100, 300, 50, 50)
zumbi = pygame.Rect(50, 500, 50, 50)
esqueleto = pygame.Rect(0, 500, 50, 50)
bandido = pygame.Rect(60, 500, 50, 50)
Troll = pygame.Rect(80, 500, 100, 100)
Boss = pygame.Rect(60, 500, 200, 200)

fonte = pygame.font.Font(None, 50)

while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
        if evento.type == pygame.MOUSEBUTTONDOWN and vida_player > 0:
            dedo_x, dedo_y = evento.pos
            vx = dados["movimento"]["player"]["player move"]["player.x"]
            vy = dados["movimento"]["player"]["player move"]["player.y"]
            if abs(dedo_x - player.x) > abs(dedo_y - player.y):
                if dedo_x > player.x:
                    player.x = player.x + vx
                else:
                    player.x = player.x - vx
            else:
                if dedo_y > player.y:
                    player.y = player.y + vy
                else:
                    player.y = player.y - vy
            if vida_zumbi > 0 and player.colliderect(zumbi):
                 vida_zumbi = vida_zumbi - dano_player
            if vida_zumbi <= 0:
                if vida_esqueleto > 0 and player.colliderect(esqueleto):
                    vida_esqueleto = vida_esqueleto - dano_player
            if vida_esqueleto <= 0:
                if vida_bandido > 0 and player.colliderect(bandido):
                    vida_bandido = vida_bandido - dano_player
            if vida_bandido <= 0:
                if vida_Troll > 0 and player.colliderect(Troll):
                    vida_Troll = vida_Troll - dano_player
            if vida_Troll <= 0:
                if vida_Boss > 0 and player.colliderect(Boss):
                    vida_Boss = vida_Boss - dano_player
    tempo_zumbi = tempo_zumbi + 1
    if tempo_zumbi >= 60 and vida_zumbi > 0:
        tempo_zumbi = 0

        zx = dados["movimento"]["zumbi"]["zumbi move"]["zumbi.x"]
        zy = dados["movimento"]["zumbi"]["zumbi move"]["zumbi.y"]
        if zumbi.x < player.x:
            zumbi.x = zumbi.x + zx
        if zumbi.x > player.x:
            zumbi.x = zumbi.x - zx
        if zumbi.y < player.y:
            zumbi.y = zumbi.y + zy
        if zumbi.y > player.y:
            zumbi.y = zumbi.y - zy
        if vida_player > 0 and zumbi.colliderect(player):
            vida_player = vida_player - dano_zumbi

    tela.fill(cores_clima[time])
    if vida_zumbi <= 0 and vida_esqueleto > 0:
            pygame.draw.rect(tela ,(230, 230, 230), esqueleto)
            tempo_esqueleto = tempo_esqueleto + 1
    if tempo_esqueleto >= 60 and vida_esqueleto > 0:
        tempo_esqueleto = 0
        ex = dados["movimento"]["esqueleto"]["esqueleto move"]["esqueleto.x"]
        ey = dados["movimento"]["esqueleto"] ["esqueleto move"]["esqueleto.y"]
        if esqueleto.x > player.x:
            esqueleto.x = esqueleto.x - ex
        if esqueleto.x < player.x:
            esqueleto.x = esqueleto.x + ex
        if esqueleto.y > player.y:
            esqueleto.y = esqueleto.y - ey
        if esqueleto.y < player.y:
            esqueleto.y = esqueleto.y + ey
        if vida_player > 0 and esqueleto.colliderect(player):
            vida_player = vida_player - dano_esqueleto
    if vida_esqueleto <= 0 and vida_bandido > 0:
        pygame.draw.rect(tela ,(3, 3, 0), bandido)
        tempo_bandido = tempo_bandido + 1
        if tempo_bandido >= 60 and vida_bandido > 0:
            tempo_bandido = 0
            bx = dados["movimento"]["bandido"]["bandido move"]["bandido.x"]
            by = dados["movimento"]["bandido"]["bandido move"]["bandido.y"]
            if bandido.x > player.x:
                bandido.x = bandido.x - bx
            if bandido.x < player.x:
                bandido.x = bandido.x + bx
            if bandido.y > player.y:
                bandido.y = bandido.y - by
            if bandido.y < player.y:
                bandido.y = bandido.y + by
            if vida_player > 0 and bandido.colliderect(player):
                vida_player = vida_player - dano_bandido
    if vida_bandido <= 0 and vida_player > 0:
        if cura: vida_player = vida_player + dados["cura"]["cura"]["player"]["vida"]
        cura = False
    if vida_bandido <= 0 and vida_Troll > 0:
        pygame.draw.rect(tela ,(100, 155, 50), Troll)
        tempo_Troll = tempo_Troll + 1
        if tempo_Troll >= 60:
            tempo_Troll = 0
            Tx = dados["movimento"]["Troll"]["Troll move"]["Troll.x"]
            Ty = dados["movimento"]["Troll"]["Troll move"]["Troll.y"]
            if Troll.x > player.x:
                Troll.x = Troll.x - Tx
            if Troll.x < player.x:
                Troll.x = Troll.x + Tx
            if Troll.y > player.y:
                Troll.y = Troll.y - Ty
            if Troll.y < player.y:
                Troll.y = Troll.y + Ty
            if vida_player > 0 and Troll.colliderect(player):
                vida_player = vida_player - dano_Troll
    if vida_Troll <= 0 and vida_Boss > 0:
        pygame.draw.rect(tela ,(200, 10, 200), Boss)
        tempo_Boss = tempo_Boss + 1
        if tempo_Boss >= 60:
            tempo_Boss = 0
            Bx = dados["movimento"]["Boss"]["Boss move"]["Boss.x"]
            By = dados["movimento"]["Boss"]["Boss move"]["Boss.y"]
            if Boss.x > player.x:
                Boss.x = Boss.x - Bx
            if Boss.x < player.x:
                Boss.x = Boss.x + Bx
            if Boss.y > player.y:
                Boss.y = Boss.y - By
            if Boss.y < player.y:
                Boss.y = Boss.y + By
            if vida_player > 0 and Boss.colliderect(player):
                vida_player = vida_player - dano_Boss
    if vida_Boss <= 0:
        texto = fonte.render("VOCE GANHOU!", True, (255, 255, 255))
        tela.blit(texto, (150, 250))
    if vida_player <= 0:
        texto = fonte.render("VOCE PERDEU!", True, (255, 255, 255))
        tela.blit(texto, (150, 250))
    if vida_zumbi > 0:
        pygame.draw.rect(tela, (10, 240, 5), zumbi)
    if vida_player > 0:
        pygame.draw.rect(tela, (250, 5, 0), player)
    pygame.display.flip()
    relogio.tick(60)

pygame.quit()

