cs=1;

if ~isempty(PDI.CoresMM{PDI.ROI.CP(1)})

    for cp=1:
        
        %toma a localização da camisa do time 
        PDI.ROI.Pos(cp,:) = PDI.T.transformPointsInverse(PDI.CoresMM{PDI.ROI.CP(1)}(cp,1:2));
        %teste para que a posição não ultra passe o valor maximo da imagem
        PDI.ROI.Xi(cp) = round(PDI.ROI.Pos(cp,2)-PDI.ROI.Tamanho);
        if PDI.ROI.Xi(cp)<1
            PDI.ROI.Xi(cp)=1;
        end
        PDI.ROI.Xf(cp) = round(PDI.ROI.Pos(cp,2)+PDI.ROI.Tamanho);
        if PDI.ROI.Xf(cp)>PDI.ROI.Xm
            PDI.ROI.Xf(cp)=PDI.ROI.Xm;
        end
        PDI.ROI.Yi(cp) = round(PDI.ROI.Pos(cp,1)-PDI.ROI.Tamanho);
        if PDI.ROI.Yi(cp)<1
            PDI.ROI.Yi(cp)=1;
        end
        PDI.ROI.Yf(cp) = round(PDI.ROI.Pos(cp,1)+PDI.ROI.Tamanho);
        if PDI.ROI.Yf(cp)>PDI.ROI.Ym
            PDI.ROI.Yf(cp)=PDI.ROI.Ym;
        end
    end
    
%Segmenta as camisas============================================================================
    
    while true
        kk = 1;
        if Cores.Usadas(cs)
            %Inicio da segmentação===================================================
            for cp=1:length(PDI.CoresMM{PDI.ROI.CP(1)}(:,1))
                % REALIZAR A SEGMENTAÇÃO EM HSV
                
                if PDI.LimitesHSV(cs,1) < PDI.LimitesHSV(cs,2)
                    PDI.Imagem.SegH (PDI.ROI.Xi(cp):PDI.ROI.Xf(cp),PDI.ROI.Yi(cp):PDI.ROI.Yf(cp)) = (PDI.Imagem.HSV(PDI.ROI.Xi(cp):PDI.ROI.Xf(cp),PDI.ROI.Yi(cp):PDI.ROI.Yf(cp),1) >= PDI.LimitesHSV(cs,1)/360) & (PDI.Imagem.HSV(PDI.ROI.Xi(cp):PDI.ROI.Xf(cp),PDI.ROI.Yi(cp):PDI.ROI.Yf(cp),1) <= PDI.LimitesHSV(cs,2)/360);
                else
                    PDI.Imagem.SegH (PDI.ROI.Xi(cp):PDI.ROI.Xf(cp),PDI.ROI.Yi(cp):PDI.ROI.Yf(cp)) = (PDI.Imagem.HSV(PDI.ROI.Xi(cp):PDI.ROI.Xf(cp),PDI.ROI.Yi(cp):PDI.ROI.Yf(cp),1) >= PDI.LimitesHSV(cs,1)/360) | (PDI.Imagem.HSV(PDI.ROI.Xi(cp):PDI.ROI.Xf(cp),PDI.ROI.Yi(cp):PDI.ROI.Yf(cp),1) <= PDI.LimitesHSV(cs,2)/360);
                end
                
                PDI.Imagem.SegS (PDI.ROI.Xi(cp):PDI.ROI.Xf(cp),PDI.ROI.Yi(cp):PDI.ROI.Yf(cp)) = (PDI.Imagem.HSV(PDI.ROI.Xi(cp):PDI.ROI.Xf(cp),PDI.ROI.Yi(cp):PDI.ROI.Yf(cp),2) >= PDI.LimitesHSV(cs,3)/100) & (PDI.Imagem.HSV(PDI.ROI.Xi(cp):PDI.ROI.Xf(cp),PDI.ROI.Yi(cp):PDI.ROI.Yf(cp),2) <= PDI.LimitesHSV(cs,4)/100);
                PDI.Imagem.SegV (PDI.ROI.Xi(cp):PDI.ROI.Xf(cp),PDI.ROI.Yi(cp):PDI.ROI.Yf(cp)) = (PDI.Imagem.HSV(PDI.ROI.Xi(cp):PDI.ROI.Xf(cp),PDI.ROI.Yi(cp):PDI.ROI.Yf(cp),3) >= PDI.LimitesHSV(cs,5)/100) & (PDI.Imagem.HSV(PDI.ROI.Xi(cp):PDI.ROI.Xf(cp),PDI.ROI.Yi(cp):PDI.ROI.Yf(cp),3) <= PDI.LimitesHSV(cs,6)/100);

                PDI.Imagem.SegTotal(PDI.ROI.Xi(cp):PDI.ROI.Xf(cp),PDI.ROI.Yi(cp):PDI.ROI.Yf(cp),cs) = medfilt2(PDI.Imagem.SegH(PDI.ROI.Xi(cp):PDI.ROI.Xf(cp),PDI.ROI.Yi(cp):PDI.ROI.Yf(cp)) & PDI.Imagem.SegS(PDI.ROI.Xi(cp):PDI.ROI.Xf(cp),PDI.ROI.Yi(cp):PDI.ROI.Yf(cp)) & PDI.Imagem.SegV(PDI.ROI.Xi(cp):PDI.ROI.Xf(cp),PDI.ROI.Yi(cp):PDI.ROI.Yf(cp))); % Eliminar Ruído Sal e Pimenta
                PDI.Imagem.SegTotal(PDI.ROI.Xi(cp):PDI.ROI.Xf(cp),PDI.ROI.Yi(cp):PDI.ROI.Yf(cp),cs) =(PDI.Imagem.SegH(PDI.ROI.Xi(cp):PDI.ROI.Xf(cp),PDI.ROI.Yi(cp):PDI.ROI.Yf(cp)) & PDI.Imagem.SegS(PDI.ROI.Xi(cp):PDI.ROI.Xf(cp),PDI.ROI.Yi(cp):PDI.ROI.Yf(cp)) & PDI.Imagem.SegV(PDI.ROI.Xi(cp):PDI.ROI.Xf(cp),PDI.ROI.Yi(cp):PDI.ROI.Yf(cp)));
                PDI.Imagem.Regioes = regionprops(PDI.Imagem.SegTotal(PDI.ROI.Xi(cp):PDI.ROI.Xf(cp),PDI.ROI.Yi(cp):PDI.ROI.Yf(cp),cs));

                for jj = 1:length(PDI.Imagem.Regioes)
                    if PDI.Imagem.Regioes(jj).Area > PDI.pPar.AreaMin
                        % Transformação para Pixel para Milimetros
                        PDI.CoresMM{cs}(kk,:) = [PDI.T.transformPointsForward( [(PDI.Imagem.Regioes(jj).Centroid(1)+PDI.ROI.Yi(cp)) (PDI.Imagem.Regioes(jj).Centroid(2)+PDI.ROI.Xi(cp))] ) PDI.Imagem.Regioes(jj).Area];
                        kk = kk + 1;
                    end
                end
                
                
            end
            %Final da segmentação===============================================
            
        end
        
        % muda a cor da camisa para a proxima
        if cs==1
            cs=4;
        elseif cs==4
            cs=6;
        elseif cs==6
            cs=7;
        else
            break
        end
    end
end


%Segmenta a bola==========================================================================

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
    
    PDI.Imagem.SegTotal(:,:,2) = (medfilt2(PDI.Imagem.SegH & PDI.Imagem.SegS & PDI.Imagem.SegV)); % Eliminar Ruído Sal e Pimenta
    
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
