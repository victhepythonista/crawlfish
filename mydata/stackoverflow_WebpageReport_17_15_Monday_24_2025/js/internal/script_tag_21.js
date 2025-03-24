
    var cam = cam || { opt: {} };
    var clcGamLoaderOptions = cam || { opt: {} };
    var opt = clcGamLoaderOptions.opt;

    opt.omni = 'BwoLCJ7ZwsqxuvU9EAUgAigBOgBIABH_Yj_xJO1DU5U';
    opt.refresh = !1;
    opt.refreshInterval = 90;
    opt.sf = !0;
    opt.hb = !1;
    opt.ll = !0;
    opt.tlb_position = 0;
    opt.personalization_consent = !1;
    opt.targeting_consent = !1;
    opt.performance_consent = !1;

    opt.targeting = {Registered:['false'],Reputation:['new'],cf_bot_score:'1'};
    opt.adReportEnabled = !0;
    opt.adReportUrl = '/ads/report-ad';
    opt.adReportText = 'Report this ad';
	opt.adReportFileTypeErrorMessage = 'Please select a PNG or JPG file.';
    opt.adReportFileSizeErrorMessage = 'The file must be under 2 MiB.';
	opt.adReportErrorText = 'Error uploading ad report.';
	opt.adReportThanksText = 'Thanks for your feedback. We’ll review this against our code of conduct and take action if necessary.';
    opt.adReportLoginExpiredMessage = 'Your login session has expired, please login and try again.';
    opt.adReportLoginErrorMessage = 'An error occurred when loading the report form - please try again';
	opt.adReportModalClass = 'js-ad-report';
    opt.countryCode = 'KE';
    opt.qualtricsSurveyData = '{"isRegistered":"False","repBucket":"new","referrer":"https%3a%2f%2fstackoverflow.com%2fquestions","accountAge":"0"}';

    opt.perRequestGuid = '491e28d6-0ca9-4869-b246-c03b6ae52798';
    opt.responseHash = 'rOS11YJ38JLftsBZdSBP/496F4/ba6RaoUaY3bhWZ54=';


    opt.targeting.TargetingConsent = ['False_Passive'];
    opt.allowAccountTargetingForThisRequest = !1;

    const urlParams = new URLSearchParams(window.location.search);
    if (urlParams.has('dfptestads')) {
        const dfptestads = urlParams.get('dfptestads');
        opt.targeting.DfpTestAds = dfptestads;
    }
