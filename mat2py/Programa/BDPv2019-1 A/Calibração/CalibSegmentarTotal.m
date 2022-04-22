%% Salva a imagem final como a soma das segmentações de cadacor

% Pré aloca a variável que irá conter as segmentações de cada cor
Calib.Imagem.SegTotal = zeros(size(Calib.Imagem.Atual,1),size(Calib.Imagem.Atual,2),8);

% Percorre todas as cores
for ii = 1:7
    % Altera a cor escolhida para cada cor
    Calib.Imagem.Cor = ii;
    
    % Faz a segmentação de cada cor
    CalibSegmentarCor
    
    % Salva cada segmentação na variável pré alocada
    Calib.Imagem.SegTotal(:,:,ii) = Calib.Imagem.Seg;
    
end

% Retorna a cor escolhida para a Total: Composição de cores em RGB
Calib.Imagem.Cor = 8;

% Realiza a soma das segmentações que contém vermelho
Calib.Imagem.Final(:,:,1) = Calib.Imagem.SegTotal(:,:,1) + Calib.Imagem.SegTotal(:,:,2) + ...
                       Calib.Imagem.SegTotal(:,:,3) + Calib.Imagem.SegTotal(:,:,7);

% Realiza a soma das segmentações que contém verde
Calib.Imagem.Final(:,:,2) = 0.5*Calib.Imagem.SegTotal(:,:,2) + Calib.Imagem.SegTotal(:,:,3) + ...
                       Calib.Imagem.SegTotal(:,:,4) + Calib.Imagem.SegTotal(:,:,5) ;

% Realiza a soma das segmentações que contém azul
Calib.Imagem.Final(:,:,3) = Calib.Imagem.SegTotal(:,:,5) + Calib.Imagem.SegTotal(:,:,6) + ...
                       Calib.Imagem.SegTotal(:,:,7) ;