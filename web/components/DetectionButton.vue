<template>
  <div
    class="imageUpload__btn detectBtn"
    v-loading="isLoading()"
    element-loading-spinner="el-icon-loading"
    element-loading-background="rgba(0, 0, 0, 0.05)"
  >
    <button class="detectBtn__detect" :disabled="isDisable()" @click="onDetect">{{buttonMsg()}}</button>
  </div>
</template>

<script>
import { mapState } from "vuex";

const DETECTION_STATE = {
  UN_UPLOADED: "UN_UPLOADED",
  UN_PROCESSED: "UN_PROCESSED",
  LOADING: "LOADING",
  SUCCESS: "SUCCESS",
  FAILURE: "FAILURE"
};

export default {
  name: "DetectionButton",
  computed: {
    ...mapState({
      btnState: state => state.video.detectionState
    })
  },
  data() {
    return {
      uploadIcon: "video-upload.png",
      disableDetectBtn: true
    };
  },
  methods: {
    isDisable() {
      return (
        this.btnState == DETECTION_STATE.UN_UPLOADED ||
        this.btnState == DETECTION_STATE.LOADING
      );
    },
    isLoading() {
      return this.btnState == DETECTION_STATE.LOADING;
    },
    buttonMsg() {
      if (this.btnState == DETECTION_STATE.FAILURE) {
        this.$notify.error({
          title: "Detection error",
          message: "Detecting video error"
        });
        return "Detect Again";
      } else if (this.btnState == DETECTION_STATE.SUCCESS) {
        this.$notify.success({
          title: "Detection success",
          message: "Detecting video success"
        });
      }

      return "Detect";
    },
    onDetect() {
      this.$store.commit("video/onDetect");
      this.uploadIcon = "image-upload.png";
    }
  }
};
</script>

<style lang='scss' scoped>
.detectBtn {
  width: 60%;
  align-self: center;
  display: flex;
  flex-flow: column nowrap;

  &__detect {
    text-transform: uppercase;
    background: $white-color;
    padding: 10px;
    border: 2px solid $red-color-light;
    display: inline-block;
    font-weight: bold;

    &:hover {
      transform: translateY(-2px) scale(1.1);
      box-shadow: 0px 2px 20px -5px rgba(0, 0, 0, 0.5);
    }

    &:disabled {
      opacity: 0.6;
      transform: scale(0.95);
    }
  }
}
</style>
