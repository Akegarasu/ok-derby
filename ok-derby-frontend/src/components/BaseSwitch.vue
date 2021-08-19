<template>
  <label class="custom-toggle">
    <input type="checkbox" v-model="model" v-bind="$attrs" v-on="$listeners" />
    <span class="custom-toggle-slider rounded-circle"></span>
  </label>
</template>
<script>
export default {
  name: "base-switch",
  inheritAttrs: false,
  props: {
    valuea: {},
  },
  model: {
    prop: "valuea",
    event: "input",
  },
  computed: {
    model: {
      get() {
        return typeof this.valuea == "boolean" ? this.valuea : true;
      },
      set(value) {
        this.$emit("input", value);
      },
    },
  },
};
</script>
<style></style>
