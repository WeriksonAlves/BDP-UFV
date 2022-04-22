[~,PWM.POS] = max(PDI.CoresMM{PDI.ROI.CP(1)}(:,3));
PWM.Pos(:,k) = PDI.CoresMM{PDI.ROI.CP(1)}(PWM.POS,1:2);