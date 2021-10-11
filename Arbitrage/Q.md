**CDS** - Креди́тный дефо́лтный своп — финансовый своп,
 покупаемый для страхования от кредитного риска,
  хотя покупатель может и не нести кредитного риска,
   либо нести его косвенно  
  ***Продажа риска (с)Степанов***  
rate стоимости cds к выплатам    
CDS spread — цена CDS в bps от номинальной цены  
  
**corporate bond spreads** - A corporate (or credit) spread is the extra interest a lender requires to compensate them for risk. The spread is measured in basis points (hundredths of a percent) over the relevant Government bond yield. The higher the perceived risk, the wider the spread  
![f](https://sun9-76.userapi.com/impg/ud-9E_m6I97FgkgYogjryzV0sMok5APM4524Jg/GFyXF-lSJeo.jpg?size=643x130&quality=96&sign=e69301f86c2d9b03a0a1d6db344bbf7c&type=album)

**VECM** - Векторная модель коррекции ошибок  
  
**bond** - облигации  
    
**Libor/OIS** - ЛИ́БОР, англ. London Interbank Offered Rate, LIBOR, ICE LIBOR) — широко распространённая эталонная процентная ставка предложения на рынке межбанковских кредитов в Лондоне, служащая ориентиром для краткосрочных процентных ставок на глобальном финансовом рынке. LIBOR рассчитывается как средняя ставка, по которой крупные международные банки предлагают необеспеченные кредиты. LIBOR рассчитывается для пяти резервных валют: доллару США, фунту стерлингов, евро, швейцарскому франку и японской иене. По каждой валюте рассчитывается индикативная процентная ставка на сроки «овернайт», одна неделя, один месяц, два месяца, три месяца, полгода и год. Таким образом, каждый рабочий день в Лондоне публикуется 35 ставок LIBOR  

What Is London Interbank Offered Rate (LIBOR)?
The London Interbank Offered Rate (LIBOR) is a benchmark interest rate at which major global banks lend to one another in the international interbank market for short-term loans.  

***Все банки берут кредиты у ЦБ (или аналога), банк покупает деньги, зачастую берутся ненадолго (1-2 дня), либор - ставка кредита на деньги    
Короче, базовая международная ставка***
### next
**Overnight indexed swap**  - An overnight indexed swap (OIS) is an interest rate swap (IRS) over some given term, e.g. 10Y, where the periodic fixed payments are tied to a given fixed rate while the periodic floating payments are tied to a floating rate calculated from a daily compounded overnight rate over the floating coupon period  

**Libor/OIS spread** - Today, the LIBOR-OIS spread is considered a key measure of credit risk within the banking sector   
***Вычитается OIS из Либора (имеется в виду OIS Rate)***
  
**ADF** - Augmented Dickey–Fuller test  
 это методика, которая используется в прикладной статистике и эконометрике для анализа временных рядов для проверки на стационарность. Является одним из тестов на единичные корни (Unit root test). Был предложен в 1979 году Дэвидом Дики и Уэйном Фуллером[1].  

 **unit root** - https://ru.wikipedia.org/wiki/%D0%95%D0%B4%D0%B8%D0%BD%D0%B8%D1%87%D0%BD%D1%8B%D0%B9_%D0%BA%D0%BE%D1%80%D0%B5%D0%BD%D1%8C  
  
**ERS** -   
**KPSS** -  Тест Квятковского — Филлипса — Шмидта — Шина (KPSS)  

***Тест Йохансена: нулевая гипотеза состоит в том, что существует максимум r; коинтеграционных векторов, альтернативная – в том, что их r+ 1. Если
величина тестов оказывается статистически значимой, то нулевая гипотеза отвергается.*** (с)Даша

***Коинтеграция - мера похожести рядов***

***Оценка параметров распределения остается постоянной - стационарность ряда***

interest risk  
expanded inflation  
**надбавки за риск:**  
default risk  
liquidity premium  
mature premium   
  
***нет звездочек - failed to reject гипотезу про no-cointegration***  
***3 ряда - все охуенно по таблице***  
***the number of lags used is determined on the basis of AIC - походу пробежался по всем и выбрал наилучшее***  
  
fig2 - колбасит во время кризиса    
Hansen fully modified  для подбора z1 и z2 и векторов  

One basis point (bps) is equal to 1/100th of 1%, or 0.01%, or 0.0001
   

Заплатить за страховку иногда лучше, чем рисковать (во время кризиса) (когда z3 < 0)

Мы можем либо купить безрисковые облигации и сидеть на низкой процентоной ставке, но это не всегда ок   
покупаем corporate bonds и cds на них   
нам это выгодно тогда, когда доходность corporate bonds с учетом страховки выше обычных безрисковых облигаций  
  
The **CDS basis** is simply the difference between the spread an investor receives when owning a physical corporate bond, and the Credit Default Swap (CDS) of the same bond. ... The basis is defined as negative when the CDS trades tighter than the physical bond spread for the same maturity.
  
  
**CDSbasis = Bond - CDS**  
Если больше нуля (или чего еще), то выгодно, иначе нет
Раньше думали, что бонд и cds коинтегрируют, но с кризисом поняли, что это не так
добавляем третий компонент, который добавляет факторы 
В этой формуле должен быть еще и Libor-ois

Короче, сделали авторегрессию, с Либор-оис закономерность круто, без него не так круто 

