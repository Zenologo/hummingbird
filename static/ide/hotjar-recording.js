(function() {
    if (typeof window.hj === 'undefined') {
        window.hj = function(){(hj.q=hj.q||[]).push(arguments)};
    }
    var DEBUG_FLAG = 'i-ss-hj-debug';
    if (!JSON.parse(window.localStorage.getItem(DEBUG_FLAG))) {
        window.localStorage.setItem(DEBUG_FLAG, 0);
    }

    var debug = !!JSON.parse(window.localStorage.getItem(DEBUG_FLAG));

    var TRIGGERED_RECORDINGS_KEY = 'i-ss-hj-triggered-recording';
    var EXCLUDED_CAMPAIGNS = "|61|218|219|220|";

    function ssLog(message, obj) {
        if (debug) {
            console.debug(message, obj)
        }
    }

    function getAdditionalPageTypes(pageType) {
        switch (pageType) {
            case 'MAIN_PRODUCT_PAGE':
            case 'OFFERS_OF_PRODUCT':
                return ['MAIN_OR_OFFERS_OF_PRODUCT_PAGES'];
            default:
                return [];

        }
    }

    function getPageTypes() {
        var pageTypes;
        if (typeof pageTypes === 'undefined') {
            pageTypes = [];
            if (window.location.pathname === '/') {
                pageTypes.push('START_PAGE');
            } else {
                if (typeof utag_data !== 'undefined') {
                    for (var i = 0; i < utag_data.length; i++) {
                        if (typeof utag_data[i].page_type === 'string') {
                            var pageType = utag_data[i].page_type;
                            pageTypes.push(pageType);
                            pageTypes = pageTypes.concat(getAdditionalPageTypes(pageType));
                            break;
                        }
                    }
                }
            }
        }
        return pageTypes;
    }

    function getVariationGroups() {
        var variationGroups = [];
        if (typeof _i_ss_data !== 'undefined') {
            _i_ss_data.counted_campaigns.forEach(function(campaignData) {
                if (EXCLUDED_CAMPAIGNS.indexOf("|" + campaignData.campaign_id + "|") === -1) {
                    variationGroups.push(campaignData.variation_group);
                }
            });
            ssLog('variation_groups:', variationGroups);
        }
        return variationGroups;
    }

    function getTriggeredRecordings() {
        var triggeredRecordings = window.sessionStorage.getItem(TRIGGERED_RECORDINGS_KEY) || "{}";
        return triggeredRecordings !== "[object Object]"
            ? JSON.parse(triggeredRecordings)
            : {};
    }

    function recordingAlreadyTriggered(variationGroup) {
        return !!getTriggeredRecordings()[variationGroup];
    }

    function markRecordingAsTriggered(variationGroup) {
        var triggeredRecordings = getTriggeredRecordings();
        triggeredRecordings[variationGroup] = 1;
        window.sessionStorage.setItem(TRIGGERED_RECORDINGS_KEY, JSON.stringify(triggeredRecordings));
    }

    function triggerRecording(variationName) {
        if (!recordingAlreadyTriggered(variationName)) {
            window.hj('trigger', variationName);
            markRecordingAsTriggered(variationName);
            ssLog('triggered recording:', variationName);
        }
    }

    function triggerHeatMap(variationName) {
        getPageTypes().forEach(function(pageType) {
            var hjEvent = pageType + '_' + variationName;
            window.hj('trigger', hjEvent);
            ssLog('triggered heatmap: ', hjEvent);
        });
    }

    getVariationGroups().forEach(function(variationGroupName) {
        triggerRecording(variationGroupName);
        triggerHeatMap(variationGroupName);
    });
})();
