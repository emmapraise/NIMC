<template>
	<div class="">
		<b-form @submit.prevent="onSubmit">
			<name @userData="userData" />
			<hr />
			<personal-data @personalData="personalData" />
			<hr />
			<medical-data @medicalData="medicalData" />
			<hr />
			<kinship-data @kinshipData="kinshipData" />
			<div class="float-right mt-2">
				<b-button type="submit" variant="success">Submit</b-button>
			</div>
		</b-form>
	</div>
</template>
<script>
import Name from '../info/Name.vue';
import PersonalData from '../info/PersonalData.vue';
import MedicalData from '../info/MedicalData.vue';
import KinshipData from '../info/KinshipData.vue';
export default {
	name: 'RegisterView',
	props: ['is_admin', 'ninInfoData'],
	components: {
		Name,
		PersonalData,
		MedicalData,
		KinshipData,
	},
	data() {
		return {
			data: {},
		};
	},
	mounted() {
		this.dispatchData();
	},
	methods: {
		userData(e) {
			console.log(e);
		},
		personalData(e) {
			console.log(e);
		},
		medicalData(e) {
			console.log(e);
		},
		kinshipData(e) {
			console.log(e);
		},
		onSubmit() {
			console.log(this.data);
		},
	},
};
</script>
