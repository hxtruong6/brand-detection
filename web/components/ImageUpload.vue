<template>
  <div class="imageUpload">
    <div class="imageUpload__dropArea dropArea">
      <h2 class="dropArea__title">Upload your video</h2>
      <p class="dropArea__info">You can upload/drop a photo or paste a URL of a video</p>
    </div>
    <div class="dropArea__video videoUpload">
      <input
        class="dropArea__input"
        type="file"
        @change="onFileChanged"
        accept="video/*"
        name="VideoUploadArea"
        id="file"
      />
      <label class="dropArea__label dropArea__label--border" for="file">
        <img :src="getImgUrl(uploadIcon)" title="Upload/drop video" />
        <br />
        <h2 v-if="!isUploaded()">Choose a video</h2>
        <h2 v-else>Video uploaded</h2>
      </label>
    </div>
    <!-- <div class="imageUpload___pasteLink pastelink">
      <h2 class="pastelink__title">Paste URL</h2>
      <input
        class="pastelink__input"
        type="text"
        placeholder="www.common-buckeye.jpg"
        title="URL image"
        @change="onPasteLink"
      />
    </div>-->
    <detection-button />
  </div>
</template>

<script>
import { mapState } from "vuex";
import DetectionButton from "~/components/DetectionButton.vue";

export default {
  name: "ImageUpload",
  components: {
    DetectionButton
  },
  computed: {
    ...mapState({
      url: state => state.video.url,
      detectedUrl: state => state.video.detectedUrl,
      loading: state => state.video.loading
    })
  },
  data() {
    return {
      uploadIcon: "video-upload.png",
      disableDetectBtn: true,
      video: this.url || ""
    };
  },
  methods: {
    isUploaded() {
      return !!this.url;
    },
    getImgUrl(pic) {
      return require("~/assets/images/" + pic);
    },
    onFileChanged(event) {
      const originVideo = event.target.files[0];
      this.uploadIcon = "uploaded.png";
      this.$store.commit("video/onFileChanged", originVideo);
      this.disableDetectBtn = false;
      this.$notify.success({
        title: "Uploading video success",
        message: "Video is ready for detecting"
      });
    },
    checkURL(url) {
      return url.match(/\.(jpeg|jpg|png)$/) != null;
    },
    onPasteLink(event) {
      const link = event.target.value;
      this.$store.commit("video/onPasteLink", link);
      this.disableDetectBtn = false;
    },

    onDetect() {
      this.$store.commit("video/onDetect");
      console.log("xx 401 loading: ", this.loading);

      this.uploadIcon = "image-upload.png";
    }
  }
};
</script>

<style lang='scss' scoped>
.imageUpload {
  background-color: $secondary-color;
  display: flex;
  justify-content: space-around;
  flex-flow: column nowrap;
  flex: 1 1 0;
  transition: all 0.2s ease;

  font-size: 1.4rem;

  &__dropArea {
  }

  .dropArea {
    display: flex;
    flex-direction: column;
    align-items: center;
    text-align: center;

    &__title {
      font-weight: bold;
      font-size: 2rem;
    }
    &__info {
    }

    &__video {
      width: 80%;
      margin: 0 auto;
    }

    &__input {
      width: 0.1px;
      height: 0.1px;
      opacity: 0;
      overflow: hidden;
      position: absolute;
      z-index: -1;
    }
    &__input + label {
      font-size: 1.3rem;
      font-weight: bold;
      // color: white;
      // display: inline-block;
      cursor: pointer;

      opacity: 0.7;
    }

    &__input:focus + label,
    &__input + label:hover {
      opacity: 1;
      font-weight: bolder;
      font-size: 1.4rem;
    }

    &__label {
      font-weight: bolder;

      margin: 5px;
      padding: 5px;
      display: flex;
      flex-flow: column nowrap;
      align-items: center;
      align-content: space-around;
      justify-content: space-around;
      &--border {
        border-top: 2px solid $primary-color-light;
        border-bottom: 2px solid $red-color-light;
        background-image: linear-gradient(
            $primary-color-light,
            $red-color-light
          ),
          linear-gradient($primary-color-light, $red-color-light);
        background-size: 2px 100%;
        background-position: 0 0, 100% 0;
        background-repeat: no-repeat;
      }
    }
  }

  .pastelink {
    margin: 0% 2%;
    &__title {
      font-weight: bold;
    }
    &__input {
      width: 100%;
    }
  }
}
</style>
