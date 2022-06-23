<template>
	<div class="">
		<b-tabs content-class="mt-3 w-75 mx-auto" justified v-model="tabIndex">
			<b-tab title="Name Data" active>
				<name />
				<div align-h="end" class="float-right mt-3">
					<b-button @click="tabIndex++" variant="outline-success">
						Next <b-icon icon="chevron-double-right"></b-icon>
					</b-button>
				</div>
			</b-tab>
			<b-tab title="Personal Data">
				<personal-data />
				<div align-h="end" class="float-right mt-3">
					<b-button-group>
						<b-button @click="tabIndex--" variant="outline-warning">
							<b-icon icon="chevron-double-left"></b-icon> Previous
						</b-button>
						<b-button @click="tabIndex++" variant="outline-success">
							Next <b-icon icon="chevron-double-right"></b-icon> </b-button
					></b-button-group>
				</div>
			</b-tab>
			<b-tab title="Medical Details">
				<medical-data />
				<div align-h="end" class="float-right mt-3">
					<b-button-group>
						<b-button @click="tabIndex--" variant="outline-warning">
							<b-icon icon="chevron-double-left"></b-icon> Previous
						</b-button>
						<b-button @click="tabIndex++" variant="outline-success">
							Next <b-icon icon="chevron-double-right"></b-icon> </b-button
					></b-button-group></div
			></b-tab>
			<b-tab title="Kinship Details">
				<kinship-data />
				<div align-h="end" class="float-right mt-3">
					<b-button @click="tabIndex--" variant="outline-warning">
						<b-icon icon="chevron-double-left"></b-icon> Previous
					</b-button>
				</div></b-tab
			>
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
