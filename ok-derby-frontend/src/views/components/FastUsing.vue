<template>
  <div>
    <div class="card">
      <div class="card-header">
        <div class="row align-items-center">
          <div class="col">
            <h3 class="mb-0">快捷操作</h3>
          </div>
          <div class="col col-md-auto">
            <badge :type="badgeType">{{ jobStat }}</badge>
          </div>
          <div class="col col-md-1 text-right">
            <base-button size="sm" type="primary" @click="showPlugins = true">
              插件
            </base-button>
          </div>
        </div>
      </div>
      <div class="card-body">
        <base-button
          type="default"
          @click="startJob('nurturing')"
          style="margin-bottom: 10px"
          >育成</base-button
        >
        <base-button
          type="primary"
          @click="startJob('nurturing', true)"
          style="margin-bottom: 10px"
          v-tooltip.top-center="
            '该选项只会加载afk插件，如果需要其他插件请使用育成手动选择插件'
          "
          >无人值守育成（全自动）</base-button
        >
        <base-button
          type="default"
          @click="startJob('daily_race_money')"
          style="margin-bottom: 10px"
          >日常-金币</base-button
        >
        <base-button
          type="default"
          @click="startJob('daily_race_sp')"
          style="margin-bottom: 10px"
          >日常-PT</base-button
        >
        <base-button
          type="default"
          style="margin-bottom: 10px"
          @click="startJob('team_race')"
          >团队赛</base-button
        >
        <base-button
          type="default"
          style="margin-bottom: 10px"
          @click="startJob('legend_race')"
          >传奇赛</base-button
        >
        <base-button
          type="default"
          style="margin-bottom: 10px"
          @click="startJob('champions_meeting')"
          >PvP 活动赛</base-button
        >
        <base-button
          type="danger"
          @click="stopJob()"
          style="margin-bottom: 10px"
          >停止</base-button
        >
      </div>
    </div>

    <div>
      <modal :show="showPlugins" @close="showPlugins = false">
        <template v-slot:header>
          <h5 class="modal-title" id="exampleModalLabel">插件列表</h5>
        </template>
        <div>
          <div
            class="row"
            v-for="i in plugins"
            :key="i.name"
            style="margin-bottom: 10px"
          >
            <div class="col">
              <p v-tooltip.left="i.description">
                {{ i.name }}
              </p>
            </div>
            <div class="col">
              <base-switch v-model="i.checked"> </base-switch>
            </div>
          </div>
        </div>
        <template v-slot:footer>
          <base-button type="secondary" @click="showPlugins = false"
            >关闭</base-button
          >
          <base-button type="primary" @click="savePlugins">保存</base-button>
        </template>
      </modal>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import CONFIG from "@/config.json";
import storage from "good-storage";
export default {
  name: "fastUsing",
  components: {},
  props: {},
  data() {
    return {
      plugins: {},
      showPlugins: false,
      jobName: "",
      jobStatus: "stopped",
    };
  },
  methods: {
    startJob(jobName, afk = false) {
      axios
        .post(CONFIG.backend + "/api/start", {
          job_name: jobName,
          plugins: afk == true ? "afk" : this.getOnPlugins(),
        })
        .then((response) => {
          if (response.data.code == 0) {
            this.$notify({
              type: "info",
              title: `添加任务${jobName}成功了哟`,
            });
          } else {
            this.$notify({
              type: "warning",
              title: `添加任务${jobName}失败`,
              message: response.data.data,
            });
          }
          console.log(response);
        });
    },
    stopJob() {
      axios.post(CONFIG.backend + "/api/stop").then((response) => {
        if (response.data.code == 0) {
          this.$notify({
            type: "info",
            title: `停止成功`,
          });
        } else {
          this.$notify({
            type: "warning",
            title: `停止失败`,
            message: response.data.data,
          });
        }
        console.log(response);
      });
    },
    loadPlugins() {
      axios
        .get(CONFIG.backend + "/api/plugins")
        .then((response) => {
          return response.data.data;
        })
        .then((data) => {
          let onPluginsList =
            storage.get("onPlugins") == undefined
              ? ""
              : storage.get("onPlugins").split(",");
          let plugins = data.map((x) => {
            if (onPluginsList.indexOf(x.name) != -1) {
              return {
                name: x.name,
                checked: true,
                description: x.description,
              };
            } else return x;
          });
          console.log(plugins);
          this.plugins = plugins;
        });
    },
    getOnPlugins() {
      let onPlugins = this.plugins
        .filter((x) => x.checked == true)
        .map((x) => x.name)
        .join(",");
      return onPlugins;
    },
    savePlugins() {
      console.log(this.plugins);
      let onPlugins = this.getOnPlugins();
      console.log(onPlugins);
      storage.set("onPlugins", onPlugins);
      this.showPlugins = false;
    },
    getJobStatus() {
      axios
        .get(CONFIG.backend + "/api/status")
        .then((response) => {
          return response.data.data;
        })
        .then((data) => {
          this.jobStatus = data.status;
          this.jobName = data.job_name;
        });
    },
  },
  mounted() {
    this.loadPlugins();
    setInterval(this.getJobStatus, 1000);
  },
  computed: {
    jobStat() {
      return this.jobStatus == "running"
        ? `当前任务：${this.jobName}`
        : "当前无任务进行中";
    },
    badgeType() {
      return this.jobStatus == "running" ? "danger" : "success";
    },
  },
};
</script>

<style lang="scss">
.tooltip {
  display: block !important;
  z-index: 10000;

  .tooltip-inner {
    background: #5e72e4;
    color: white;
    border-radius: 6px;
    padding: 5px 10px 4px;
  }

  .tooltip-arrow {
    width: 0;
    height: 0;
    border-style: solid;
    position: absolute;
    margin: 5px;
    border-color: #5e72e4;
    z-index: 1;
  }

  &[x-placement^="top"] {
    margin-bottom: 15px;

    .tooltip-arrow {
      border-width: 5px 5px 0 5px;
      border-left-color: transparent !important;
      border-right-color: transparent !important;
      border-bottom-color: transparent !important;
      bottom: -5px;
      left: calc(50% - 5px);
      margin-top: 0;
      margin-bottom: 0;
    }
  }

  &[x-placement^="bottom"] {
    margin-top: 5px;

    .tooltip-arrow {
      border-width: 0 5px 5px 5px;
      border-left-color: transparent !important;
      border-right-color: transparent !important;
      border-top-color: transparent !important;
      top: -5px;
      left: calc(50% - 5px);
      margin-top: 0;
      margin-bottom: 0;
    }
  }

  &[x-placement^="right"] {
    margin-left: 5px;

    .tooltip-arrow {
      border-width: 5px 5px 5px 0;
      border-left-color: transparent !important;
      border-top-color: transparent !important;
      border-bottom-color: transparent !important;
      left: -5px;
      top: calc(50% - 5px);
      margin-left: 0;
      margin-right: 0;
    }
  }

  &[x-placement^="left"] {
    margin-right: 20px;

    .tooltip-arrow {
      border-width: 5px 0 5px 5px;
      border-top-color: transparent !important;
      border-right-color: transparent !important;
      border-bottom-color: transparent !important;
      right: -5px;
      top: calc(50% - 5px);
      margin-left: 0;
      margin-right: 0;
    }
  }

  &[aria-hidden="true"] {
    visibility: hidden;
    opacity: 0;
    transition: opacity 0.15s, visibility 0.15s;
  }

  &[aria-hidden="false"] {
    visibility: visible;
    opacity: 1;
    transition: opacity 0.15s;
  }
}
</style>
