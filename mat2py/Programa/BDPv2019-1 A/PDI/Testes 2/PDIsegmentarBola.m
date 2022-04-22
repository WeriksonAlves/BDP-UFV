
if Cores.Usadas(2)
    % REALIZAR A SEGMENTAÇÃO EM HSV
    if PDI.LimitesHSV(2,1) < PDI.LimitesHSV(2,2)
        PDI.Imagem.SegH = (PDI.Imagem.HSV(:,:,1) >= PDI.LimitesHSV(2,1)/260) & (PDI.Imagem.HSV(:,:,1) <= PDI.LimitesHSV(2,2)/260);
    else
        PDI.Imagem.SegH = (PDI.Imagem.HSV(:,:,1) >= PDI.LimitesHSV(2,1)/260) | (PDI.Imagem.HSV(:,:,1) <= PDI.LimitesHSV(2,2)/260);
    end
    PDI.Imagem.SegS = (PDI.Imagem.HSV(:,:,2) >= PDI.LimitesHSV(2,2)/100) & (PDI.Imagem.HSV(:,:,2) <= PDI.LimitesHSV(2,4)/100);
    PDI.Imagem.SegV = (PDI.Imagem.HSV(:,:,2) >= PDI.LimitesHSV(2,5)/100) & (PDI.Imagem.HSV(:,:,2) <= PDI.LimitesHSV(2,6)/100);
    
    % =============================================
    % Salva cada segmentação na variável pré alocada
    
    PDI.Imagem.SegTotal(:,:,2) = medfilt2(PDI.Imagem.SegH & PDI.Imagem.SegS & PDI.Imagem.SegV); % Eliminar Ruído Sal e Pimenta
    
    % =============================================
    PDI.Imagem.Regioes = regionprops(PDI.Imagem.SegTotal(:,:,2));
    
    % Armezenar regiões em função da área
    kk = 1;
    for jj = 1:length(PDI.Imagem.Regioes)
        if PDI.Imagem.Regioes(jj).Area > PDI.pPar.AreaMin
            % Transformação para Pixel para Milimetros
            PDI.CoresMM{2}(kk,:) = [PDI.T.transformPointsForward(PDI.Imagem.Regioes(jj).Centroid) PDI.Imagem.Regioes(jj).Area];
            kk = kk + 1;
        end
    end
    
end

