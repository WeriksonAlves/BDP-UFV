
if Cores.Usadas(PDI.ROI.CP(2))
    % REALIZAR A SEGMENTAÇÃO EM HSV
    if PDI.LimitesHSV(PDI.ROI.CP(2),1) < PDI.LimitesHSV(PDI.ROI.CP(2),2)
        PDI.Imagem.SegH = (PDI.Imagem.HSV(:,:,1) >= PDI.LimitesHSV(PDI.ROI.CP(2),1)/360) & (PDI.Imagem.HSV(:,:,1) <= PDI.LimitesHSV(PDI.ROI.CP(2),2)/360);
    else
        PDI.Imagem.SegH = (PDI.Imagem.HSV(:,:,1) >= PDI.LimitesHSV(PDI.ROI.CP(2),1)/360) | (PDI.Imagem.HSV(:,:,1) <= PDI.LimitesHSV(PDI.ROI.CP(2),2)/360);
    end
    PDI.Imagem.SegS = (PDI.Imagem.HSV(:,:,2) >= PDI.LimitesHSV(PDI.ROI.CP(2),3)/100) & (PDI.Imagem.HSV(:,:,2) <= PDI.LimitesHSV(PDI.ROI.CP(2),4)/100);
    PDI.Imagem.SegV = (PDI.Imagem.HSV(:,:,3) >= PDI.LimitesHSV(PDI.ROI.CP(2),5)/100) & (PDI.Imagem.HSV(:,:,3) <= PDI.LimitesHSV(PDI.ROI.CP(2),6)/100);
    
    % =============================================
    % Salva cada segmentação na variável pré alocada
    
    PDI.Imagem.SegTotal(:,:,PDI.ROI.CP(2)) = medfilt2(PDI.Imagem.SegH & PDI.Imagem.SegS & PDI.Imagem.SegV); % Eliminar Ruído Sal e Pimenta
    
    % =============================================
    PDI.Imagem.Regioes = regionprops(PDI.Imagem.SegTotal(:,:,PDI.ROI.CP(2)));
    
    % Armezenar regiões em função da área
    kk = 1;
    for jj = 1:length(PDI.Imagem.Regioes)
        if PDI.Imagem.Regioes(jj).Area > PDI.pPar.AreaMin
            % Transformação para Pixel para Milimetros
            PDI.CoresMM{PDI.ROI.CP(2)}(kk,:) = [PDI.T.transformPointsForward(PDI.Imagem.Regioes(jj).Centroid) PDI.Imagem.Regioes(jj).Area];
            kk = kk + 1;
        end
    end
    
end