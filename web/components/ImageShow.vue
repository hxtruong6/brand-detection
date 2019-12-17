<template>
  <div class="imageShow">
    <div class="imageShow__area image">
      <div class="image__toggle">
        <h3
          class="imageView"
          :class="{'selected' : isOriginImg==true}"
          @click="selectOriginImg(true)"
        >Origin Image</h3>
        <div v-if="detectedUrl">/</div>
        <h3
          class="imageView"
          :class="{'selected' : isOriginImg==false}"
          v-if="detectedUrl"
          @click="selectOriginImg(false)"
        >Detected Image</h3>
      </div>
      <img class="image__display" :src="getDisplayImg()" />
    </div>
    <div class="imageShow__history history">
      <div class="history__title">History</div>
    </div>
  </div>
</template>

<script>
import { mapState } from "vuex";

export default {
  name: "ImageShow",
  computed: {
    ...mapState({
      detectedImage: state => state.image.detectedImage,
      url: state => state.image.url,
      detectedUrl: state => state.image.detectedUrl
    }),
    defaultImg() {
      return require("~/assets/images/brandTag.png");
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
      this.$store.commit("image/getResult");
    }
  },
  methods: {
    getImgUrl(pic) {
      return require("~/assets/images/" + pic);
    },
    getDisplayImg() {
      return this.isOriginImg && this.url
        ? this.url
        : !this.isOriginImg && this.detectedUrl
        ? this.detectedUrl
        : this.defaultImg;
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
      width: auto;
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
