% Analisa os estados dos Checkboxes e habilita janelas

% ====================================
% C�mera
if BDP.menu(1).Value    
    set(Cam.ID,'Visible','on','Position',[1 1 0.2 1].*BDP.DimTela,...
        'OuterPosition',[1 1 0.2 1].*BDP.DimTela + [0 50 0 -80] + [BDP.DimTela(3)*0.2 0 0 0]);
else
    CamTelaFechar
end

% ====================================
% Calibra��o de Cores
if BDP.menu(2).Value
    CalibTelaAbrir
    CalibProcessarImagem
else
    CalibTelaFechar
end

% ====================================
% Calibra��o do Campo
if BDP.menu(3).Value
    CampoTelaAbrir
else
    CampoTelaFechar
end

% ====================================
% Modo partida
if BDP.menu(4).Value
    PartidaTelaAbrir
else
    PartidaTelaFechar
end

% ====================================
% Teste PWM
if BDP.menu(5).Value
    PWMTelaAbrir
else
    PWMTelaFechar
end
