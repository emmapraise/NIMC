<template>
	<div class="">
		<b-form @submit.prevent="onSubmit">
			<name @userData="userData" :getData="ninInfoData" :isAdmin="isAdmin" />
			<hr />
			<personal-data
				@personalData="personalData"
				:isAdmin="isAdmin"
				:getData="ninInfoData"
			/>
			<hr />
			<medical-data
				@medicalData="medicalData"
				:isAdmin="isAdmin"
				:getData="ninInfoData"
			/>
			<hr />
			<kinship-data
				@kinshipData="kinshipData"
				:isAdmin="isAdmin"
				:getData="ninInfoData"
			/>
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
	props: ['isAdmin', 'ninInfoData'],
	components: {
		Name,
		PersonalData,
		MedicalData,
		KinshipData,
	},
	data() {
		return {
			data: {},
			userDispatch: {
				user: {},
			},
		};
	},
	mounted() {
		this.loadData();
	},
	methods: {
		loadData() {
			this.userDispatch = this.ninInfoData.citizen;
		},
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
