<template>
  <div class="imageInfo">
    <div class="imageInfo__display" v-if="hasResult()">
      <img width="128px" :src="brand.logo" />
      <div class="imageInfo__name">
        <span>Name:</span>
        {{name}}
      </div>
      <div class="imageInfo__time">
        <span>Predicted in:</span>
        {{second}} seconds
      </div>
      <div class="imageInfo__confidence">
        <span>Confidence:</span>
        {{confidence}}
      </div>
      <div class="imageInfo__percentCover">
        <span>Percent cover:</span>
        {{percentCover}}
      </div>
      <div class="imageInfo__description">
        <span>Description:</span>
        {{brand.description}}
      </div>
    </div>
    <div class="imageInfo__notify" v-if="!hasResult()">
      <div>No information</div>
      <div style="color: red">{{result.message}}</div>
    </div>
  </div>
</template>

<script>
import { mapState } from "vuex";

export default {
  name: "ImageInfo",
  computed: {
    ...mapState({
      result: state => state.video.result,
      butterfly: state => {
        // console.log("xxx 320 state: ", state);
        if (state.video.result && state.video.result.name) {
          const name = state.video.result.name;
          // console.log("xxx 325 keys: ", Object.keys(state.butterfly.data));
          const butterfly = Object.keys(state.butterfly.data).find(
            b => b.toLowerCase() === name.toLowerCase()
          );
          // console.log("xxx 305 butterfly: ", butterfly);
          return state.butterfly.data[butterfly] || {};
        }
      },
      brand: state => {
        if (state.video.result && state.video.result.name) {
          const name = state.video.result.name;
          const nameMapping = Object.keys(state.brand.data).find(
            b => b.toLowerCase() === name.toLowerCase()
          );
          return state.brand.data[nameMapping];
        }
        return {};
      }
    })
  },
  data() {
    return {
      name: "",
      second: "",
      confidence: "",
      percentCover: ""
    };
  },
  watch: {
    result: function(val) {
      console.log("xxx 310 result change: ", val);
      const { name, second, confidence, percentCover } = val;
      this.name = name;
      this.second = second;
      this.confidence = confidence;
      this.percentCover = percentCover;
    }
  },
  methods: {
    hasResult() {
      console.log("xxx512 has result: ", this.result);
      return this.result && this.result.ok;
    }
  }
};
</script>

<style lang='scss' scoped>
.imageInfo {
  flex: 1.5 1 0;
  background-color: $third-color-light;
  font-size: 1.8rem;
  display: flex;
  justify-content: center;

  &__display {
    margin: 4px;
    display: flex;
    flex-flow: column nowrap;
    justify-content: space-around;
    span {
      font-weight: bold;

      &:hover {
        font-weight: bolder;
      }
    }
    &__link {
      text-decoration: none;
      text-decoration-color: $third-color;
      cursor: pointer;
      transition: all 0.2s ease;

      &:hover {
        text-decoration: underline;
        font-style: italic;
        transform: translate(-1px) scale(1.05);
      }
    }
  }
  &__percentCover {
    font-size: 2.5rem;
    background-color: #a1dbf8;
    padding: 5px;
    border-radius: 3px;
  }
  &__notify {
    margin: auto;
  }
}
</style>
