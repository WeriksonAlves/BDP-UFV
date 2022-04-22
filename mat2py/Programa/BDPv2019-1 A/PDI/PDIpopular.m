% Identificação das cores
% 1- Red
% 2- Orange
% 3- Yellow
% 4- Green
% 5- Cyan
% 6- Blue
% 7- Magenta

% ============================================
% Posicionar Bola
% Busca por maior área encontrada
if ~isempty(PDI.CoresMM)
    if ~isempty(PDI.CoresMM{2})
        [~,Bola.maxArea] = max(PDI.CoresMM{2}(:,3));
        Bola.X = PDI.CoresMM{2}(Bola.maxArea,1:2);
    end
    % ============================================
    
    % Popular jogadores adversários
    % Determinar número de robôs adversários
    
    switch JogAdv(1).pTime
        % ============================================
        case 'y' % Yellow
            if ~isempty(PDI.CoresMM{3})
                for ii = 1:size(PDI.CoresMM{3},1)
                    JogAdv(ii).pPos.X = PDI.CoresMM{3}(ii,1:2)';
%                     PDI.ROI.POSIDEN(2,ii) = 1;
                end
            end
        case 'c' % Cyan
            if ~isempty(PDI.CoresMM{5})
                for ii = 1:size(PDI.CoresMM{5},1)
                    JogAdv(ii).pPos.X = PDI.CoresMM{5}(ii,1:2)';
%                     PDI.ROI.POSIDEN(2,ii) = 1;
                end
            end
            
    end
    for ii = 1:3
        switch JogBDP(ii).pTime
            % ============================================
            case 'y' % Yellow
                % Popular jogadores
                % Escolha da cor por proximidade
                if ~isempty(PDI.CoresMM{3})
                    switch JogBDP(ii).pCor
                        case 'r' % Índice: 1
                            if ~isempty(PDI.CoresMM{1})
                                JogBDP(ii).pPos.X = DeterminarProximidade(JogBDP(ii).pPos.X,PDI.CoresMM{3}(:,1:2),PDI.CoresMM{1}(:,1:2));
%                                 PDI.ROI.POSIDEN(1,ii) = 1;
                            else
%                                 PDI.ROI.POSIDEN(1,ii) = 0;
                            end
                        case 'g' % Índice: 4
                            if ~isempty(PDI.CoresMM{4})
                                JogBDP(ii).pPos.X = DeterminarProximidade(JogBDP(ii).pPos.X,PDI.CoresMM{3}(:,1:2),PDI.CoresMM{4}(:,1:2));

                            else

                            end
                        case 'b' % Índice: 6
                            if ~isempty(PDI.CoresMM{6})
                                JogBDP(ii).pPos.X = DeterminarProximidade(JogBDP(ii).pPos.X,PDI.CoresMM{3}(:,1:2),PDI.CoresMM{6}(:,1:2));

                            else

                            end
                        case 'm' % Índice: 7
                            if ~isempty(PDI.CoresMM{7})
                                JogBDP(ii).pPos.X = DeterminarProximidade(JogBDP(ii).pPos.X,PDI.CoresMM{3}(:,1:2),PDI.CoresMM{7}(:,1:2));

                            else

                            end
                    end
                end
                
                % ============================================
            case 'c' % Cyan
                % Popular jogadores
                % Escolha da cor por proximidade
                if ~isempty(PDI.CoresMM{5})
                    switch JogBDP(ii).pCor
                        case 'r' % Índice: 1
                            if ~isempty(PDI.CoresMM{1})
                                JogBDP(ii).pPos.X = DeterminarProximidade(JogBDP(ii).pPos.X,PDI.CoresMM{5}(:,1:2),PDI.CoresMM{1}(:,1:2));

                            else

                            end
                        case 'g' % Índice: 4
                            if ~isempty(PDI.CoresMM{4})
                                JogBDP(ii).pPos.X = DeterminarProximidade(JogBDP(ii).pPos.X,PDI.CoresMM{5}(:,1:2),PDI.CoresMM{4}(:,1:2));

                            else

                            end
                        case 'b' % Índice: 6
                            if ~isempty(PDI.CoresMM{6})
                                JogBDP(ii).pPos.X = DeterminarProximidade(JogBDP(ii).pPos.X,PDI.CoresMM{5}(:,1:2),PDI.CoresMM{6}(:,1:2));

                            else

                            end
                        case 'm' % Índice: 7
                            if ~isempty(PDI.CoresMM{7})
                                JogBDP(ii).pPos.X = DeterminarProximidade(JogBDP(ii).pPos.X,PDI.CoresMM{5}(:,1:2),PDI.CoresMM{7}(:,1:2));

                            else

                            end
                    end
                end
        end
    end
end

% =========================================================================
function Pos = DeterminarProximidade(Pos,A,B)
% Filtar por distância: D = 150mm
% Distância entre o centro do robô e sua camisa

id = [0 0];
D = 200;
for  ii = 1:size(A,1)
    for  jj = 1:size(B,1)
        d = norm(A(ii,1:2)-B(jj,1:2));
        if D > d
            D = d;
            id = [ii jj];
        end
    end
end

if sum(id) > 1
    % Posição do jogador
    Pos(1:2,1) = mean([A(id(1),1:2);B(id(2),1:2)])';
    
    % CORRIGIR: Singularidade entre -180 e 180
    % Orientação do jogador
    psi = atan2(B(id(2),2)-A(id(1),2),B(id(2),1)-A(id(1),1));
    Pos(3,1) = psi;
    

    
end

end
