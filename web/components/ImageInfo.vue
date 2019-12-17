<template>
  <div class="imageInfo">
    <div class="imageInfo__wrap" v-if="items.length">
      <div class="imageInfo__display" v-for="(item, i) in items" v-bind:key="item.key">
        <img width="64px" :src="item.brand.logo" />
        <div class="imageInfo__name">
          <span>Name:</span>
          {{item.name}}
        </div>
        <div class="imageInfo__confidence">
          <span>Confidence:</span>
          {{item.confidence}}%
        </div>
        <div class="imageInfo__description">
          <span>Description:</span>
          {{item.brand.description}}
        </div>
        <div class="imageInfo__break" v-show="i!=items.length-1" />
      </div>
    </div>
    <div class="imageInfo__notify" v-else>
      <img width="80%" src="https://i.imgur.com/jtkTPvb.gif?noredirect" />
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
      result: state => state.image.result,
      brand: state => state.brand.data
    })
  },
  data() {
    return {
      items: []
    };
  },
  watch: {
    result: function(vals) {
      console.log("xx500 vals: ", vals);
      if (!vals.ok) return;
      const { data } = vals;
      this.items = [];
      console.log("xx501 vals: ", data);
      Object.keys(data).forEach((item, i) => {
        const { class: name, confidence } = data[item];
        this.items.push({
          key: `img_res_${i}`,
          name,
          confidence: (confidence * 100).toFixed(2),
          brand: this.brand[String(name).toLowerCase()]
        });
      });
      console.log("xxx 502 tesm: ", this.items);
    }
  }
};
</script>

<style lang='scss' scoped>
.imageInfo {
  flex: 1.5 1 0;
  flex-flow: column;
  background-color: $third-color-light;
  font-size: 1.5rem;
  display: flex;
  justify-content: center;

  &__wrap {
    overflow: scroll;
  }

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
    text-align: center;
    font-size: 2rem;
  }

  &__break {
    height: 3px;
    background-color: $third-color-dark;
  }
}
</style>
