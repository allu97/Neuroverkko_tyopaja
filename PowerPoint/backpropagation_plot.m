x = -5:0.05:5;
y = 50*x.^2;
hold on
figure_123 = plot(x,y, 'b','LineWidth',2)
plot([0 0],ylim, '--r', 'LineWidth', 1)
set(gca,'XTick',[], 'YTick', [])
%title('')
xlabel('Painokerroin','FontName','Times','FontSize',12,'FontWeight','bold','Color','#EDB120', 'Position', [4 0]);
ylabel('Virhe','FontName','Times','FontSize',12,'FontWeight','bold','Color','#EDB120')
annotation('arrow',[.13 .94],[.11 .11])
annotation('arrow',[.131 .131],[.13 .97])
text(-0.5,-80,'Minimi','FontName','Times','FontSize',12,'FontWeight','bold')
text(-5,300,'Nosta painoarvoa','FontName','Times','FontSize',10,'FontWeight','bold')
text(2.6,300,'Laske painoarvoa','FontName','Times','FontSize',10,'FontWeight','bold')
%% Plot arrow and dot to (3.5,y(3,5))
plot(3.5,50*3.5^2,'r*','LineWidth', 2)
annotation('arrow',[.78 .7],[.47 .47])
text(2.7,700,'---','Color','r','FontName','Times','FontSize',18,'FontWeight','bold')

plot(2.5,50*2.5^2,'r*','LineWidth', 2)
annotation('arrow',[.705 .625],[.293 .293])
text(1.9,400,'--','Color','r','FontName','Times','FontSize',18,'FontWeight','bold')

plot(1.5,50*1.5^2,'r*','LineWidth', 2)
annotation('arrow',[.63 .55],[.175 .175])
text(0.95,200,'-','Color','r','FontName','Times','FontSize',18,'FontWeight','bold')
%% Plot arrow and dot to (-3.5,y(-3.5))
plot(-3.5,50*(-3.5)^2,'r*','LineWidth', 2)
annotation('arrow',[.255 .325],[.47 .47])
text(-3.5,700,'+++','Color','g','FontName','Times','FontSize',16,'FontWeight','bold')

plot(-2.5,50*(-2.5)^2,'r*','LineWidth', 2)
annotation('arrow',[.33 .41],[.293 .293])
text(-2.35,400,'++','Color','g','FontName','Times','FontSize',16,'FontWeight','bold')

plot(-1.5,50*(-1.5)^2,'r*','LineWidth', 2)
annotation('arrow',[.41 .49],[.175 .175])
text(-1.25,200,'+','Color','g','FontName','Times','FontSize',16,'FontWeight','bold')
