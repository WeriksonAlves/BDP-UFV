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
    
   PDI.Imagem.Final=zeros(size(PDI.Imagem.RGB));

    
    if Cores.Usadas(1)==1 %Red
        PDI.Imagem.Final(:,:,1)=PDI.Imagem.Final(:,:,1)+PDI.Imagem.SegTotal(:,:,1);
    end

    if Cores.Usadas(2)==1 %Orange
        PDI.Imagem.Final(:,:,1)=PDI.Imagem.Final(:,:,1)+PDI.Imagem.SegTotal(:,:,2);
        PDI.Imagem.Final(:,:,2)=PDI.Imagem.Final(:,:,2)+0.5*PDI.Imagem.SegTotal(:,:,2);
    end

    if Cores.Usadas(3)==1 %Yellow
        PDI.Imagem.Final(:,:,1)=PDI.Imagem.Final(:,:,1)+PDI.Imagem.SegTotal(:,:,3);
        PDI.Imagem.Final(:,:,2)=PDI.Imagem.Final(:,:,2)+PDI.Imagem.SegTotal(:,:,3);
    end

    if Cores.Usadas(4)==1 %Green
        PDI.Imagem.Final(:,:,2)=PDI.Imagem.Final(:,:,2)+PDI.Imagem.SegTotal(:,:,4);
    end

    if Cores.Usadas(5)==1 %Cyan
        PDI.Imagem.Final(:,:,2)=PDI.Imagem.Final(:,:,2)+PDI.Imagem.SegTotal(:,:,5);
        PDI.Imagem.Final(:,:,3)=PDI.Imagem.Final(:,:,3)+PDI.Imagem.SegTotal(:,:,5);
    end

    if Cores.Usadas(6)==1 %Blue
        PDI.Imagem.Final(:,:,3)=PDI.Imagem.Final(:,:,3)+PDI.Imagem.SegTotal(:,:,6);
    end

    if Cores.Usadas(7)==1 %Magenta
        PDI.Imagem.Final(:,:,1)=PDI.Imagem.Final(:,:,1)+ PDI.Imagem.SegTotal(:,:,7);
        PDI.Imagem.Final(:,:,3)=PDI.Imagem.Final(:,:,3)+ PDI.Imagem.SegTotal(:,:,7);
    end
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

