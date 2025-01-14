<template>
  <v-table theme="dark">
    <thead>
      <tr>
        <th class="text-left">Username</th>
        <th class="text-left">Timezone</th>
        <th class="text-left">Is Active?</th>
        <th class="text-left">Last Update At</th>
        <th class="text-left">Created At</th>
        <th class="text-left">Actions</th>
      </tr>
    </thead>
    <tbody></tbody>
  </v-table>
</template>
<script lang="ts">
export default {
  data() {
    return {
      desserts: [
        {
          name: "Frozen Yogurt",
          calories: 159,
        },
        {
          name: "Ice cream sandwich",
          calories: 237,
        },
        {
          name: "Eclair",
          calories: 262,
        },
        {
          name: "Cupcake",
          calories: 305,
        },
        {
          name: "Gingerbread",
          calories: 356,
        },
        {
          name: "Jelly bean",
          calories: 375,
        },
        {
          name: "Lollipop",
          calories: 392,
        },
        {
          name: "Honeycomb",
          calories: 408,
        },
        {
          name: "Donut",
          calories: 452,
        },
        {
          name: "KitKat",
          calories: 518,
        },
      ],
    };
  },
};
</script>
