import FileSaver from 'file-saver';

export const state = () => ({
    originImage: null,
    detectedImage: null,
    url: null,
    detectedUrl: null,
    result: {},
    loading: false,
});

export const mutations = {
    onFileChanged(state, originImage) {
        state.originImage = originImage;
        state.url = URL.createObjectURL(originImage);
    },
    async onPasteLink(state, link) {
        state.loading = true;
        console.log('xxx 400 loading: ', state.loading);

        await fetch(link)
            .then((res) => res.blob()) // Gets the response and returns it as a blob
            .then((blob) => {
                let objectURL = URL.createObjectURL(blob);
                state.url = objectURL;

                const file = new File([blob], `${new Date().getTime()}.jpg`, {
                    type: 'image/png',
                });
                state.originImage = file;
            });

        console.log('xxx 403 blob: ', state.originImage);
        state.loading = false;
        console.log('xxx 401 loading: ', state.loading);
    },
    async onDetect(state) {
        if (!state.originImage) return;
        console.log('xxx 406 originImage: ', state.originImage);

        let formData = new FormData();
        formData.append('file', state.originImage);
        state.loading = true;
        await this.$axios
            .post('image', formData, {
                responseType: 'blob',
                headers: {
                    'Content-Type': 'multipart/form-data',
                },
                onDownloadProgress: function(progressEvent) {
                    console.log(
                        'download',
                        progressEvent.loaded,
                        progressEvent.total,
                    );
                },
                onUploadProgress: (progressEvent) =>
                    console.log(progressEvent.loaded),
            })
            .then((res) => {
                console.log('DETECT SUCCESS!! ', res);
                const blob = new Blob([res.data], { type: 'image/*' });
                const url = URL.createObjectURL(blob);
                state.detectedImage = blob;
                state.detectedUrl = url;
                // FileSaver.saveAs(blob, `prediction.jpg`);
            })
            .catch(() => {
                console.log('DETECT FAILURE!!');
            })
            .finally(() => {
                state.loading = false;
            });
    },
    async getResult(state) {
        await this.$axios
            .get('result')
            .then((res) => {
                console.log('GET SUCCESS: ', res);
                console.log('xxx 300 type of data: ', typeof res.data);
                state.result = res.data;
            })
            .catch((e) => {
                console.log('GET FAILURE!!');
            });
    },
};
