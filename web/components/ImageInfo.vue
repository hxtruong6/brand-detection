<template>
  <div class="imageInfo">
    <div class="imageInfo__display" v-if="name">
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
      <div class="imageInfo__description">
        <span>Description:</span>
        {{butterfly.description}}
      </div>
      <a class="imageInfo__link" :href="butterfly.link" target="_blank">Detail more...</a>
    </div>
    <div class="imageInfo__notify" v-if="!name&&!second">No information</div>
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
      }
    })
  },
  data() {
    return {
      name: "",
      second: "",
      confidence: ""
    };
  },
  watch: {
    result: function(val) {
      console.log("xxx 310 result change: ", val);
      const { name, second, confidence } = val;
      this.name = name;
      this.second = second;
      this.confidence = confidence;
    }
  }
};
</script>

<style lang='scss' scoped>
.imageInfo {
  flex: 1.5 1 0;
  background-color: $third-color-light;
  font-size: 1.5rem;
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

  &__notify {
    margin: auto;
  }
}
</style>
