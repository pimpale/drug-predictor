% Actual data points mapped from https://www.ncbi.nlm.nih.gov/books/NBK294310/figure/ch2.f1/?report=objectonly
x = 1900:10:2010;
x = [x 2012];
y = [50 100 700 1500 1800 3600 4000 4000 3900 2750 2000 1300 1250];
plot(x, y);
hold();

% Fitting a fourth order polynomial to model cigarette usage over time
p = polyfit(x, y, 4);
x2 = 1960:2050;
y2 = polyval(p, x2);
plot(x, y, 'o', x2, y2);
title("Cigarette Use");
xlabel("Year");
ylabel("Per capita number of cigarettes smoked per year");

%{
% https://www.mathworks.com/matlabcentral/answers/303800-how-to-use-euler-s-method-to-solve-the-logistic-grown-model
t = 2012:2032;
y0 = 1250;
dt = 1;

y = zeroes(size(t));
y(1) = y0;


for k = 2 : numel(t)
    y(k) = y(k-1) + () * dt
end
%}
