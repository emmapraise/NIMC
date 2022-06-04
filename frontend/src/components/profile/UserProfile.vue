<template>
	<div class="container">
		<b-tabs content-class="mt-3 w-50 mx-auto" justified>
			<b-tab title="Name" active>
				<name />
			</b-tab>
			<b-tab title="Personal Data">
				<personal-data />
				<b-button @click="done">Submit</b-button>
			</b-tab>
			<b-tab title="Medical Details"> <medical-data /></b-tab>
			<b-tab title="Kinship Details"> <kinship-data /> </b-tab>
		</b-tabs>
	</div>
</template>
<script>
import Name from '../info/Name.vue';
import PersonalData from '../info/PersonalData.vue';
import MedicalData from '../info/MedicalData.vue';
import KinshipData from '../info/KinshipData.vue';
export default {
	name: 'RegisterView',
	components: {
		Name,
		PersonalData,
		MedicalData,
		KinshipData,
	},
	data() {
		return {};
	},
	mounted() {
		console.log('object');
		this.done();
	},
	methods: {
		done() {
			console.log(this.personal_data_tab);
		},
	},
};
</script>
