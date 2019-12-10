import FileSaver from "file-saver";

const DETECTION_STATE = {
    UN_UPLOADED: "UN_UPLOADED",
    UN_PROCESSED: "UN_PROCESSED",
    LOADING: "LOADING",
    SUCCESS: "SUCCESS",
    FAILURE: "FAILURE"
};

const dumpBrand = {
    name: "dasani",
    confidence: "90%",
    second: 45,
    percentCover: "60%"
};

export const state = () => ({
    originVideo: null,
    detectedImage: null,
    url: null,
    detectedUrl: null,
    result: { ok: false },
    loading: false,
    detectionState: DETECTION_STATE.UN_UPLOADED
});

export const mutations = {
    onFileChanged(state, originVideo) {
        state.originVideo = originVideo;
        state.url = URL.createObjectURL(originVideo);
        state.detectionState = DETECTION_STATE.UN_PROCESSED;
    },
    async onPasteLink(state, link) {
        state.loading = true;
        console.log("xxx 400 loading: ", state.loading);

        await fetch(link)
            .then(res => res.blob()) // Gets the response and returns it as a blob
            .then(blob => {
                let objectURL = URL.createObjectURL(blob);
                state.url = objectURL;

                const file = new File([blob], `${new Date().getTime()}.jpg`, {
                    type: "video/*"
                });
                state.originVideo = file;
            });
        state.loading = false;
        state.detectionState = DETECTION_STATE.UN_PROCESSED;
    },
    async onDetect(state) {
        if (!state.originVideo) return;
        console.log("xxx 406 originVideo: ", state.originVideo);

        let formData = new FormData();
        formData.append("file", state.originVideo);
        state.loading = true;
        state.detectionState = DETECTION_STATE.LOADING;

        await this.$axios
            .post("video", formData, {
                responseType: "blob",
                headers: {
                    "Content-Type": "multipart/form-data"
                },
                onDownloadProgress: function(progressEvent) {
                    console.log(
                        "download",
                        progressEvent.loaded,
                        progressEvent.total
                    );
                },
                onUploadProgress: progressEvent =>
                    console.log(progressEvent.loaded)
            })
            .then(res => {
                console.log("DETECT SUCCESS!! ", res);
                const blob = new Blob([res.data], { type: "video/*" });
                const url = URL.createObjectURL(blob);
                state.detectedImage = blob;
                state.detectedUrl = url;
                state.detectionState = DETECTION_STATE.SUCCESS;
                // FileSaver.saveAs(blob, `prediction.jpg`);
            })
            .catch(err => {
                console.log("DETECT FAILURE!! ", err);
                state.result = {
                    ok: false,
                    message: "Detecting video error"
                };
                state.detectionState = DETECTION_STATE.FAILURE;
            })
            .finally(() => {
                state.loading = false;
            });
    },
    async getResult(state) {
        // state.result = { ok: true, ...dumpBrand };
        await this.$axios
            .get("result")
            .then(res => {
                console.log("GET SUCCESS: ", res);
                console.log("xxx 300 type of data: ", typeof res.data);
                state.result = { ok: true, ...res.data };
            })
            .catch(e => {
                console.log("GET FAILURE!!");
                state.result = {
                    ok: false,
                    message: "Get result from server error"
                };
            });
    }
};
