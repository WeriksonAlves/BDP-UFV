%Salva o número do jogador que será utilizado para o teste
PWM.NJog = PWM.B(4).Value;

%Area minima a ser considerada pleo PDI
PDI.pPar.AreaMin = 20;

%Indica que está no modo de coleta de dados
PWM.ObterDados=1;

k=1;
%Variavel usada para salvar a posição do jogador no teste "k"
PWM.Pos=[];
%Variavel de tempo para indicar o tempo de cada captura
PWM.TempoTotal=tic;
PWM.TempoAmostra=tic;

%Iniciar comunicação ================================
ComunicacaoIniciar

if get(Partida.CorTime(1),'Value')
    PDI.ROI.CP(1)=3;
    Cores.Usadas = [0 0 1 0 0 0 0];
else
    PDI.ROI.CP(1)=5;
    Cores.Usadas = [0 0 0 0 1 0 0];
end

while PWM.ObterDados
    if toc(PWM.TempoAmostra) > 0.2
        
        %Segmentar a imagem
        PWMSegmentar
        %Enaviar dados para o jogador ==============================
        PWMEnviar
        %Encontrar a localização do jogador e salvar
        PWMPosicao
        k = k+1;
        
        %Exibir imagem
        if PWM.SegImOn.Value
            PWMExibirImagem
        end 
        
        %Atualizar tempo do jogo
        PWM.T(5).String = strcat('Tempo entre amostras: ' , num2str(toc(PWM.TempoAmostra)));
        PWM.T(6).String = strcat('Tempo de teste: ' , num2str(toc(PWM.TempoTotal)));
        PWM.TempoAmostra=tic;
        
        %teste de limite de tempo
        if str2num(get(PWM.B(9),'String')) > 0 && toc(PWM.TempoTotal) > str2num(get(PWM.B(9),'String')) 
            PWMCaptura
        end
        
        drawnow
    end 
end
