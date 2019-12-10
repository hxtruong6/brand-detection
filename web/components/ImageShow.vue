<template>
  <div class="imageShow">
    <div class="imageShow__area image">
      <div class="image__toggle">
        <h3
          class="imageView"
          :class="{'selected' : isOriginImg==true}"
          @click="selectOriginImg(true)"
        >Origin Video</h3>
        <div v-if="detectedUrl">/</div>
        <h3
          class="imageView"
          :class="{'selected' : isOriginImg==false}"
          v-if="detectedUrl"
          @click="selectOriginImg(false)"
        >Detected Video</h3>
      </div>
      <!-- <img class="image__display" :src="getDisplayImg()" /> -->
      <div class="image__display">
        <video width="100%" controls :src="getDisplaySource()" id="videoId"></video>
      </div>
    </div>
    <!-- <div class="imageShow__history history">
      <div class="history__title">History</div>
    </div>-->
  </div>
</template>

<script>
import { mapState } from "vuex";

export default {
  name: "ImageShow",
  computed: {
    ...mapState({
      detectedImage: state => state.video.detectedImage,
      url: state => {
        console.log("xxx124 state video: ", state.video);
        return state.video.url;
      },
      detectedUrl: state => state.video.detectedUrl
    }),
    defaultImg() {
      return "https://nature.mdc.mo.gov/sites/default/files/styles/centered_full/public/webform/2018/Common%20Buckeye-20181011-2222.jpeg";
    }
  },
  data: function() {
    return {
      isOriginImg: true
    };
  },
  watch: {
    detectedUrl: function() {
      this.isOriginImg = false;
      this.$store.commit("video/getResult");
    }
    // url: function() {
    //   console.log("xxx 004 upload video end: ", this.state.video);
    //   return this.state.video.url;
    // }
  },
  methods: {
    getImgUrl(pic) {
      return require("~/assets/images/" + pic);
    },
    getDisplaySource() {
      // console.log("xxx004 state Video: ", this.state.video);
      // console.log("xxx005 display: ", this.isOriginImg, this.url);
      return this.url;
      // return this.isOriginImg && this.url
      //   ? this.url
      //   : !this.isOriginImg && this.detectedUrl
      //   ? this.detectedUrl
      //   : this.defaultImg;
    },
    selectOriginImg(value) {
      this.isOriginImg = Boolean(value);
    }
  }
};
</script>

<style lang='scss' scoped>
.imageShow {
  display: flex;
  flex-flow: column nowrap;
  flex: 2 1 0;
  font-size: 1.5rem;
  // padding: 4px;

  &__area,
  .image {
    flex: 3 1 0;
    display: flex;
    flex-flow: column nowrap;
    align-content: center;
    justify-content: center;

    &__toggle {
      margin: 4px;
      top: 2px;
      position: absolute;
      display: flex;
      font-weight: bold;

      cursor: pointer;

      .imageView {
        margin: 1px;
        opacity: 0.8;
        transition: all 0.2s ease;

        &:hover {
          opacity: 1;
          transform: translate(-2px) scale(1.05);
          font-weight: bolder;
        }
      }
      .selected {
        text-decoration: underline;
        text-decoration-color: $primary-color;
      }
    }

    &__display {
      align-self: center;
      // padding: 10px;
      max-height: 85%;
      width: 90%;
    }
  }

  &__history,
  .history {
    flex: 1 1 0;
    background-color: $red-color-light;

    &__title {
      padding: 4px;
    }
  }
}
</style>
