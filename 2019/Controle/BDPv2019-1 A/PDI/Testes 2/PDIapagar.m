for cp=1:length(PDI.ROI.Xi)
    PDI.Imagem.SegTotal(PDI.ROI.Xi(cp):PDI.ROI.Xf(cp),PDI.ROI.Yi(cp):PDI.ROI.Yf(cp),1)=0;
    PDI.Imagem.SegTotal(PDI.ROI.Xi(cp):PDI.ROI.Xf(cp),PDI.ROI.Yi(cp):PDI.ROI.Yf(cp),4)=0;
    PDI.Imagem.SegTotal(PDI.ROI.Xi(cp):PDI.ROI.Xf(cp),PDI.ROI.Yi(cp):PDI.ROI.Yf(cp),6)=0;
    PDI.Imagem.SegTotal(PDI.ROI.Xi(cp):PDI.ROI.Xf(cp),PDI.ROI.Yi(cp):PDI.ROI.Yf(cp),7)=0;
end

for cp=1:length(PDI.ROI.PAXi)
    PDI.Imagem.SegTotal(PDI.ROI.PAXi(cp):PDI.ROI.PAXf(cp),PDI.ROI.PAYi(cp):PDI.ROI.PAYf(cp),3)=0;
    PDI.Imagem.SegTotal(PDI.ROI.PAXi(cp):PDI.ROI.PAXf(cp),PDI.ROI.PAYi(cp):PDI.ROI.PAYf(cp),5)=0;
end

for cp=1:length(PDI.ROI.PCXi)
    PDI.Imagem.SegTotal(PDI.ROI.PCXi(cp):PDI.ROI.PCXf(cp),PDI.ROI.PCYi(cp):PDI.ROI.PCYf(cp),3)=0;
    PDI.Imagem.SegTotal(PDI.ROI.PCXi(cp):PDI.ROI.PCXf(cp),PDI.ROI.PCYi(cp):PDI.ROI.PCYf(cp),5)=0;
end