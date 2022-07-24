<template>
	<div class="">
		<b-row>
			<b-col
				class="my-1"
				v-for="(item, index) in medical_tab"
				:key="index"
				md="6"
			>
				<b-row>
					<b-col md="4">
						<label :for="item.label">{{ item.name }} </label>
					</b-col>
					<b-col md="8">
						<template v-if="edit">
							<div v-if="item.type === 'select'">
								<b-form-select
									:id="item.label"
									v-model="item.value"
									@change="emitValue"
									required
									:options="item.options"
								></b-form-select>
							</div>
						</template>
						<template v-else>{{ item.value }}</template></b-col
					></b-row
				>
			</b-col>
		</b-row>
	</div>
</template>
<script>
export default {
	name: 'MedicalDataComponent',
	props: {
		isAdmin: Boolean,
		getData: Object,
		edit: Boolean,
	},
	data() {
		return {
			medical_tab: [
				{
					name: 'Blood Group',
					label: 'blood_group',
					value: null,
					options: [
						{ value: null, text: 'Select a Option' },
						{ value: 'A', text: 'A' },
						{ value: 'B', text: 'B' },
						{ value: 'AB', text: 'AB' },
						{ value: 'O', text: 'O' },
					],
					type: 'select',
				},
				{
					name: 'Genotype',
					label: 'genotype',
					value: null,
					type: 'select',
					options: [
						{ value: null, text: 'Select a Option' },
						{ value: 'AA', text: 'AA' },
						{ value: 'AS', text: 'AS' },
						{ value: 'AC', text: 'AC' },
						{ value: 'SS', text: 'SS' },
					],
				},
			],
		};
	},
	mounted() {
		if (!this.isAdmin) {
			this.loadData();
		}
	},
	methods: {
		emitValue() {
			const data = this.medical_tab.reduce(
				(acc, cur) => ({ ...acc, [cur.label]: cur.value }),
				{}
			);
			this.$emit('medicalData', data);
		},
		loadData() {
			this.medical_tab.map((item) => {
				const asArray = Object.entries(this.getData);
				const filtered = asArray.filter(([key]) => key === item['label']);
				const justStrings = Object.fromEntries(filtered);
				return (item['value'] = justStrings[item['label']]);
			});
		},
	},
};
</script>
