% =========================================================================
% Imagem câmera
if get(Partida.Visual(1),'Value')
    axes(Partida.Cam.ID)
    Partida.Cam.fig = imshow(PDI.Imagem.RGB,'parent',Partida.Cam.ID);
    set(Partida.Cam.ID,'Position',[0/3 0 1/3 0.9])
end

% =========================================================================
% Imagem segmentada
if get(Partida.Visual(2),'Value')
    axes(Partida.Seg.ID)
    % Realiza a soma das segmentações que contém vermelho
    PDI.Imagem.Final(:,:,1) = PDI.Imagem.SegTotal(:,:,1) + PDI.Imagem.SegTotal(:,:,2) + ...
        PDI.Imagem.SegTotal(:,:,3) + PDI.Imagem.SegTotal(:,:,7);
    
    % Realiza a soma das segmentações que contém verde
    PDI.Imagem.Final(:,:,2) = 0.5*PDI.Imagem.SegTotal(:,:,2) + PDI.Imagem.SegTotal(:,:,3) + ...
        PDI.Imagem.SegTotal(:,:,4) + PDI.Imagem.SegTotal(:,:,5) ;
    
    % Realiza a soma das segmentações que contém azul
    PDI.Imagem.Final(:,:,3) = PDI.Imagem.SegTotal(:,:,5) + PDI.Imagem.SegTotal(:,:,6) + ...
        PDI.Imagem.SegTotal(:,:,7) ;
    
    Partida.Seg.fig = imshow(PDI.Imagem.Final,'parent',Partida.Seg.ID);
    set(Partida.Seg.ID,'Position',[1/3 0 1/3 0.9])
end

% =========================================================================
% Exibir Jogadores e Bola no campo de Jogo
if get(Partida.Visual(3),'Value')
    for ii = 1:3
        JogBDP(ii).mCADplotar(Partida.Ass.ID);
        JogAdv(ii).mCADplotar(Partida.Ass.ID);
    end
    
    Bola.idCAD.Vertices = ([1 0 Bola.X(1); 0 1 Bola.X(2); 0 0 1]*Bola.CAD)';
    set(Partida.Ass.ID,'Position',[2/3 0 1/3 0.9])
end