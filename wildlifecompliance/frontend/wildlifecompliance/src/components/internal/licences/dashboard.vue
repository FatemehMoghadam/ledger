<template>
<div class="container" id="internalDash">
    <LicenceDashTable level="internal" :url="licences_url"/>
</div>
</template>
<script>
import LicenceDashTable from '@common-utils/licences_dashboard.vue'
import {
  api_endpoints,
  helpers
}
from '@/utils/hooks'
export default {
    name: 'InternalLicenceDashboard',
    data() {
        let vm = this;
        return {
            licences_url: api_endpoints.licences,
        }
    
    },
    watch: {},
    components: {
        LicenceDashTable,
    },
    computed: {
    },
    methods: {},
    mounted: function () {
    }
}
</script>
