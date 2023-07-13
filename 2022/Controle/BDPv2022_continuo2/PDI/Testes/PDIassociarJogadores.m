% Associar jogadores com base nas camisas obtidas pelo processamento de
% imagem. O objetivo é minimizar a distância coletiva entre os jogadores e
% as camisas encontradas
%
% Alguns filtros são aplicados para excluir situações como:
% -> Camisa distânte do jogados
% -> Dois jogadores com a mesma camisa
%
% O algoritmo proposto não está otimizado. Requer atenção no futuro.
% Versão: 26/10/2018

% ==============================
% Entende-se por jogador da Equipe BDP, aquele que possuir a cor
% estabelecida no início da partida.
% Entende-se por camisa, a cor definida para cada jogador da Equipe BDP

% Dados dos jogadores
% PDI.XJog = posição dos jogadores no campo de jogo [mm]
% PDI.XNum = posição das camisas no campo de jogo [mm]

% ===================================
% Rotina para teste
% nc = input('Num Jogadores: ');
% nn = input('Num Camisas: ');
% 
% figure
% axis([-10 10 -10 10])
% hold
% 
% PDI.XJog = ginput(nc);
% plot(PDI.XJog(:,1),PDI.XJog(:,2),'*b'),
% PDI.XNum = ginput(nn);
% plot(PDI.XNum(:,1),PDI.XNum(:,2),'sr')
% PDI.CoresNum = 'mrgmrgmrg'; 
% ===================================

% Possíveis permutações de jogadores e camisas
PDI.pemuta = [3 2 1; 3 1 2; 2 3 1; 2 1 3; 1 3 2; 1 2 3];
% Identificação do Jogador com a Camisa
PDI.idJogNum = [0 0 0];
PDI.dmin = 10000;
PDI.distJC = 1; % Distância máxima entre a identificação da camisa e do jogador


tic

PDI.nXj = size(PDI.XJog,1);
PDI.nXc = size(PDI.XNum,1);

PDI.D = zeros(PDI.nXj,PDI.nXc);
%%
for  ii = 1:PDI.nXj
    for  jj = 1:PDI.nXc
        PDI.D(ii,jj) = norm(PDI.XJog(ii,:)-PDI.XNum(jj,:));
    end
end

% Número de Jogadores menor que o número de camisas
if PDI.nXj <= PDI.nXc
    switch PDI.nXj
        case 1
            PDI.dmin = 10000;
            % Caso de um jogador e n-camisas
            for  ii = 1:PDI.nXj
                PDI.idJogNum = [0 0 0];
                if PDI.dmin > PDI.D(1,ii)
                    PDI.idJogNum = [ii 0 0];
                    PDI.dmin = PDI.D(1,ii);
                end
            end
            
        case 2
            PDI.dmin = 10000;
            % Caso de dois jogador e n-camisas
            for  ii = 1:PDI.nXc
                PDI.idJogNum = [0 0 0];
                for  jj = 1:PDI.nXc
                    if ii ~= jj
                        if PDI.dmin > PDI.D(1,ii)+PDI.D(2,jj)
                            PDI.idJogNum = [ii jj 0];
                            PDI.dmin = PDI.D(1,ii)+PDI.D(2,jj);
                        end
                    end
                end
            end
            
        case 3
            PDI.idJogNum = [0 0 0];
            PDI.dmin = 10000;
            % Caso completo de jogadores e camisas
            for  ii = 1:PDI.nXc
                for  jj = 1:PDI.nXc
                    for  kk = 1:PDI.nXc
                        if ii ~= jj && ii ~= kk && jj ~= kk
                            if PDI.dmin > PDI.D(1,ii)+PDI.D(2,jj)+PDI.D(3,kk)
                                PDI.idJogNum = [ii jj kk];
                                PDI.dmin = PDI.D(1,ii)+PDI.D(2,jj)+PDI.D(3,kk);
                            end
                        end
                    end
                end
            end
            
    end
else
    % Situação de identificar mais jogadores que camisas
    switch PDI.nPDI.XJog
        case 1 % Uma camisa
            PDI.dmin = 10000;
            for  ii = 1:PDI.nXj
                if PDI.dmin > PDI.D(ii,1)
                    PDI.idJogNum = [0 0 0];
                    PDI.idJogNum(ii) = 1;
                    PDI.dmin = PDI.D(ii,1);
                end
            end
            
            % Relacioanr camisa e jogador:  Possível falha
        case 2 % Duas camisas
            PDI.dmin = 10000;
            for ii = 1:size(PDI.pemuta,1)
                if PDI.dmin > PDI.D(PDI.pemuta(ii,1),1)+PDI.D(PDI.pemuta(ii,2),2)
                    PDI.idJogNum = [0 0 0];
                    PDI.idJogNum(p(ii,1)) = 1;
                    PDI.idJogNum(p(ii,2)) = 2;
                    PDI.idJogNum(p(ii,3)) = 0;
                    PDI.dmin = PDI.D(PDI.pemuta(ii,1),1)+PDI.D(PDI.pemuta(ii,2),2);
                end
            end
    end
end
toc

% ===================================
% for mm = 1:size(PDI.XJog,1)
%     if PDI.idJogNum(mm) > 0
%         h(mm)   = plot([PDI.XJog(mm,1) PDI.XNum(PDI.idJogNum(mm),1)],[PDI.XJog(mm,2) PDI.XNum(PDI.idJogNum(mm),2)]);
%         tx(mm)  = text(PDI.XJog(mm,1),PDI.XJog(mm,2),['Xc_{' num2str(mm) '}']);
%         txd(mm) = text(PDI.XNum(PDI.idJogNum(mm),1),PDI.XNum(PDI.idJogNum(mm),2),['Xn_{' num2str(PDI.idJogNum(mm)) '}']);
%     end
% end
% ===================================

% Transformação de Pixel para Milímetros
% Campo.Padrao.pxTeste = PDI.T.transformPointsForward(Campo.Real.pxTeste(1:2));
