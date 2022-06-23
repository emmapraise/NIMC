<template>
	<div class="">
		<name />
		<hr />
		<personal-data />
		<hr />
		<medical-data />
		<hr />
		<kinship-data />
	</div>
</template>
<script>
import Name from '../info/Name.vue';
import PersonalData from '../info/PersonalData.vue';
import MedicalData from '../info/MedicalData.vue';
import KinshipData from '../info/KinshipData.vue';
export default {
	name: 'RegisterView',
	props: ['is_admin'],
	components: {
		Name,
		PersonalData,
		MedicalData,
		KinshipData,
	},
	data() {
		return {
			tabIndex: 0,
		};
	},
	mounted() {
		this.done();
	},
	methods: {},
};
</script>
