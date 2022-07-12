<template>
	<div>
		<header-vue />
		<b-row class="mt-2">
			<b-col md="2">
				<sidebar-vue :userType="userType" />
			</b-col>
			<b-col md="10">
				<b-card title="Citizen NIN Information">
					<name-vue :getData="data" :isAdmin="false" />
					<hr />
					<personal-data-vue :getData="data" :isAdmin="false" />
					<hr />
					<medical-data-vue :getData="data" :isAdmin="false" />
					<hr />
					<kinship-data-vue :getData="data" :isAdmin="false" />
				</b-card>
			</b-col>
		</b-row>
	</div>
</template>
<script>
import HeaderVue from '@/components/header/Header.vue';
import SidebarVue from '@/components/sidebar/Sidebar.vue';
import NameVue from '@/components/info/Name.vue';
import PersonalDataVue from '@/components/info/PersonalData.vue';
import MedicalDataVue from '@/components/info/MedicalData.vue';
import KinshipDataVue from '@/components/info/KinshipData.vue';
export default {
	name: 'PatnerUserView',
	components: {
		HeaderVue,
		SidebarVue,
		NameVue,
		PersonalDataVue,
		MedicalDataVue,
		KinshipDataVue,
	},
	data() {
		return {
			data: {},
			userType: 'patner',
		};
	},
	created() {
		this.data = JSON.parse(localStorage.getItem('nininfo'));
	},
};
</script>
