%% Chama a fun��o para segmentar uma cor individualmente

% REALIZAR A SEGMENTA��O EM HSV
%Matiz
if Calib.LimitesHSV(Calib.Imagem.Cor,1) < Calib.LimitesHSV(Calib.Imagem.Cor,2)
    Calib.Imagem.SegH = (Calib.Imagem.Atual(:,:,1) >= Calib.LimitesHSV(Calib.Imagem.Cor,1)/360) & (Calib.Imagem.Atual(:,:,1) <= Calib.LimitesHSV(Calib.Imagem.Cor,2)/360);
else
    Calib.Imagem.SegH = (Calib.Imagem.Atual(:,:,1) >= Calib.LimitesHSV(Calib.Imagem.Cor,1)/360) | (Calib.Imagem.Atual(:,:,1) <= Calib.LimitesHSV(Calib.Imagem.Cor,2)/360);
end
%Satura��o
Calib.Imagem.SegS = (Calib.Imagem.Atual(:,:,2) >= Calib.LimitesHSV(Calib.Imagem.Cor,3)/100) & (Calib.Imagem.Atual(:,:,2) <= Calib.LimitesHSV(Calib.Imagem.Cor,4)/100);
%Luminosidade
Calib.Imagem.SegV = (Calib.Imagem.Atual(:,:,3) >= Calib.LimitesHSV(Calib.Imagem.Cor,5)/100) & (Calib.Imagem.Atual(:,:,3) <= Calib.LimitesHSV(Calib.Imagem.Cor,6)/100);
%Uni�o das segmenta��es
  Calib.Imagem.Seg  = Calib.Imagem.SegH & Calib.Imagem.SegS & Calib.Imagem.SegV;

% Pr� aloca a vari�vel que ir� conter a segmenta��o da cor escolhida
Calib.Imagem.Final = zeros(size(Calib.Imagem.Atual,1),size(Calib.Imagem.Atual,2),3);

% Verifica qual cor foi escolhida
switch Calib.Imagem.Cor
    case 1
        % Se for vermelho, a imagem final conter� apenas vermelho
        Calib.Imagem.Final(:,:,1) = Calib.Imagem.Seg;
        
    case 2
        % Se for laranja, a imagem final conter� vermelho e meio verde
        Calib.Imagem.Final(:,:,1) = Calib.Imagem.Seg;
        Calib.Imagem.Final(:,:,2) = 0.5 * Calib.Imagem.Seg;
        
    case 3
        % Se for amarelo, a imagem final conter� vermelho e verde
        Calib.Imagem.Final(:,:,1) = Calib.Imagem.Seg;
        Calib.Imagem.Final(:,:,2) = Calib.Imagem.Seg;
        
    case 4
        % Se for verde, a imagem final conter� apenas verde
        Calib.Imagem.Final(:,:,2) = Calib.Imagem.Seg;
        
    case 5
        % Se for ciano, a imagem final conter� verde e azul
        Calib.Imagem.Final(:,:,2) = Calib.Imagem.Seg;
        Calib.Imagem.Final(:,:,3) = Calib.Imagem.Seg;
        
    case 6
        % Se for azul, a imagem final conter� apenas azul
        Calib.Imagem.Final(:,:,3) = Calib.Imagem.Seg;
        
    case 7
        % Se for magenta, a imagem final conter� vermelho e azul
        Calib.Imagem.Final(:,:,1) = Calib.Imagem.Seg;
        Calib.Imagem.Final(:,:,3) = Calib.Imagem.Seg;
end