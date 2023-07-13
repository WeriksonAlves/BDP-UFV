
for jj=1:3
    %localiza a posi��o de cada jogador levando em considera��o sua posi��o anterior
    PDI.ROI.Pos(jj,:) = PDI.T.transformPointsInverse(JogAdv(jj).pPos.X(1:2)');
    
    %impedi que a posi��o do jogador exceda o tamanho da imagem
    PDI.ROI.PXi(jj) = round(PDI.ROI.Pos(jj,2)-PDI.ROI.TamanhoP);
    if PDI.ROI.PXi(jj)<1
        PDI.ROI.PXi(jj)=1;
    end
    PDI.ROI.PCXf(jj) = round(PDI.ROI.Pos(jj,2)+PDI.ROI.TamanhoP);
    if PDI.ROI.PCXf(jj)>PDI.ROI.Xm
        PDI.ROI.PCXf(jj)=PDI.ROI.Xm;
    end
    PDI.ROI.PCYi(jj) = round(PDI.ROI.Pos(jj,1)-PDI.ROI.TamanhoP);
    if PDI.ROI.PCYi(jj)<1
        PDI.ROI.PCYi(jj)=1;
    end
    PDI.ROI.PCYf(jj) = round(PDI.ROI.Pos(jj,1)+PDI.ROI.TamanhoP);
    if PDI.ROI.PCYf(jj)>PDI.ROI.Ym
        PDI.ROI.PCYf(jj)=PDI.ROI.Ym;
    end
end



kk = 1;
if Cores.Usadas(PDI.ROI.CP(2))
    %realiza a segmenta��o em HSV das 3 regioes encontradas 
    for cp=1:3
        if PDI.LimitesHSV(PDI.ROI.CP(2),1) < PDI.LimitesHSV(PDI.ROI.CP(2),2)
            PDI.Imagem.SegH(PDI.ROI.PXi(cp):PDI.ROI.PCXf(cp),PDI.ROI.PCYi(cp):PDI.ROI.PCYf(cp)) = (PDI.Imagem.HSV(PDI.ROI.PXi(cp):PDI.ROI.PCXf(cp),PDI.ROI.PCYi(cp):PDI.ROI.PCYf(cp),1) >= PDI.LimitesHSV(PDI.ROI.CP(2),1)/360) & (PDI.Imagem.HSV(PDI.ROI.PXi(cp):PDI.ROI.PCXf(cp),PDI.ROI.PCYi(cp):PDI.ROI.PCYf(cp),1) <= PDI.LimitesHSV(PDI.ROI.CP(2),2)/360);
        else
            PDI.Imagem.SegH(PDI.ROI.PXi(cp):PDI.ROI.PCXf(cp),PDI.ROI.PCYi(cp):PDI.ROI.PCYf(cp)) = (PDI.Imagem.HSV(PDI.ROI.PXi(cp):PDI.ROI.PCXf(cp),PDI.ROI.PCYi(cp):PDI.ROI.PCYf(cp),1) >= PDI.LimitesHSV(PDI.ROI.CP(2),1)/360) | (PDI.Imagem.HSV(PDI.ROI.PXi(cp):PDI.ROI.PCXf(cp),PDI.ROI.PCYi(cp):PDI.ROI.PCYf(cp),1) <= PDI.LimitesHSV(PDI.ROI.CP(2),2)/360);
        end
        PDI.Imagem.SegS(PDI.ROI.PXi(cp):PDI.ROI.PCXf(cp),PDI.ROI.PCYi(cp):PDI.ROI.PCYf(cp)) = (PDI.Imagem.HSV(PDI.ROI.PXi(cp):PDI.ROI.PCXf(cp),PDI.ROI.PCYi(cp):PDI.ROI.PCYf(cp),2) >= PDI.LimitesHSV(PDI.ROI.CP(2),3)/100) & (PDI.Imagem.HSV(PDI.ROI.PXi(cp):PDI.ROI.PCXf(cp),PDI.ROI.PCYi(cp):PDI.ROI.PCYf(cp),2) <= PDI.LimitesHSV(PDI.ROI.CP(2),4)/100);
        PDI.Imagem.SegV(PDI.ROI.PXi(cp):PDI.ROI.PCXf(cp),PDI.ROI.PCYi(cp):PDI.ROI.PCYf(cp)) = (PDI.Imagem.HSV(PDI.ROI.PXi(cp):PDI.ROI.PCXf(cp),PDI.ROI.PCYi(cp):PDI.ROI.PCYf(cp),3) >= PDI.LimitesHSV(PDI.ROI.CP(2),5)/100) & (PDI.Imagem.HSV(PDI.ROI.PXi(cp):PDI.ROI.PCXf(cp),PDI.ROI.PCYi(cp):PDI.ROI.PCYf(cp),3) <= PDI.LimitesHSV(PDI.ROI.CP(2),6)/100);
        
        % =============================================
        % Salva cada segmenta��o na vari�vel pr� alocada
        
        PDI.Imagem.SegTotal(PDI.ROI.PXi(cp):PDI.ROI.PCXf(cp),PDI.ROI.PCYi(cp):PDI.ROI.PCYf(cp),PDI.ROI.CP(2)) = medfilt2( PDI.Imagem.SegH(PDI.ROI.PXi(cp):PDI.ROI.PCXf(cp),PDI.ROI.PCYi(cp):PDI.ROI.PCYf(cp)) & PDI.Imagem.SegS(PDI.ROI.PXi(cp):PDI.ROI.PCXf(cp),PDI.ROI.PCYi(cp):PDI.ROI.PCYf(cp)) & PDI.Imagem.SegV(PDI.ROI.PXi(cp):PDI.ROI.PCXf(cp),PDI.ROI.PCYi(cp):PDI.ROI.PCYf(cp))); % Eliminar Ru�do Sal e Pimenta
    end
    % localiza a posi��o dos jogadores
    PDI.Imagem.Regioes = regionprops(PDI.Imagem.SegTotal(:,:,PDI.ROI.CP(2)));
    
    % Armezenar regi�es em fun��o da �rea  
    for ll = 1:length(PDI.Imagem.Regioes) % analisa todas as regioes 
        if PDI.Imagem.Regioes(ll).Area > PDI.pPar.AreaMin % testa o tamanho minimo da area
            % Transforma��o para Pixel para Milimetros
            PDI.CoresMM{PDI.ROI.CP(2)}(kk,:) = [PDI.T.transformPointsForward( [(PDI.Imagem.Regioes(ll).Centroid(1)) (PDI.Imagem.Regioes(ll).Centroid(2))] ) PDI.Imagem.Regioes(ll).Area];
            kk = kk + 1; % n�mero de localiza��es validas
        end
    end
end



