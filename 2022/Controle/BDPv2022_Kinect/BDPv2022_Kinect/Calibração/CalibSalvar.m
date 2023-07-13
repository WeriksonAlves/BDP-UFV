% Atribuir os limites HSV estipulados na calibação para a  variável PDI, a
% qual será utlizada em modo JOGO
PDI.LimitesHSV = Calib.LimitesHSV;

LimitesHSV = Calib.LimitesHSV;
save('Arquivos/LimitesHSV.mat','LimitesHSV')

