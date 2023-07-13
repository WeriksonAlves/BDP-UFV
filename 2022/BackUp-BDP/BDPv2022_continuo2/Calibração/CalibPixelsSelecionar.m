%% Determina��o dos pixels a serem utilizados na segmenta��o

% Desabilita o bot�o de selecionar pixels
set(Calib.Pixels.Botao(1),'enable','off')

% Salva os valores das cores dos pixels selecionados em RGB
Calib.Pixels.Valores = [Calib.Pixels.Valores;impixel];

% Habilita o bot�o de selecionar pixels
set(Calib.Pixels.Botao(1),'enable','on')

% Exclui os pixels selecionados fora da imagem
for ii = size(Calib.Pixels.Valores,1):-1:1
    if isnan(Calib.Pixels.Valores(ii,:))
        Calib.Pixels.Valores(ii,:) = [];
    end
end

% Verifica se foi selecionado algum pixel v�lido
if ~isempty(Calib.Pixels.Valores)
    
    % Habilita o bot�o de segmentar pixels
    set(Calib.Pixels.Botao(2),'enable','on')
    
end

% Habilita a fun��o de zoom
zoom on