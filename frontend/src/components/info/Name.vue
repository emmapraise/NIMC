<template>
	<div class="">
		<b-row>
			<b-col md="6" v-for="(item, index) in name_tab" :key="index" class="my-1">
				<b-row>
					<b-col md="4">
						<label :for="item.label">{{ item.name }}</label></b-col
					>
					<b-col md="8">
						<template v-if="isAdmin">
							<div v-if="item.type === 'radio'">
								<b-form-radio-group
									:id="item.label"
									v-model="item.value"
									required
									@input="emitValue"
									:options="item.options"
								></b-form-radio-group>
							</div>
							<div v-else>
								<b-form-input
									:id="item.label"
									:type="item.type"
									@input="emitValue"
									v-model="item.value"
									required
								></b-form-input>
							</div>
						</template>
						<template v-else>
							{{ item.value }}
						</template>
					</b-col></b-row
				></b-col
			></b-row
		>
	</div>
</template>
<script>
export default {
	name: 'NameComponet',
	props: ['getData', 'isAdmin'],
	data() {
		return {
			name_tab: [
				{
					name: 'Surname',
					label: 'last_name',
					type: 'text',
					value: '',
				},
				{
					name: 'First Name',
					label: 'first_name',
					type: 'text',
					value: '',
				},
				{
					name: 'Middle Name',
					label: 'middle_name',
					type: 'text',
					value: '',
				},
				{
					name: 'Gender',
					label: 'gender',
					type: 'radio',
					value: null,
					options: [
						{ value: 'M', text: 'Male' },
						{ value: 'F', text: 'Female' },
					],
				},
				{
					name: 'Email',
					label: 'email',
					type: 'email',
					value: '',
				},
				{
					name: 'Phone',
					label: 'phone',
					type: 'tel',
					value: '',
				},
			],
		};
	},
	mounted() {
		this.loadData();
	},
	methods: {
		emitValue() {
			const data = this.name_tab.reduce(
				(acc, cur) => ({ ...acc, [cur.label]: cur.value }),
				{}
			);
			this.$emit('userData', data);
		},
		loadData() {
			this.name_tab.map((obj) => {
				Object.keys(this.getData.citizen.user).map((item) => {
					if (obj.label === item) {
						obj.value = this.getData.citizen.user[item];
					}
				});
			});
		},
	},
};
</script>
