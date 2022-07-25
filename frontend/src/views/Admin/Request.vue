<template>
	<div>
		<header-vue :logout="true" />
		<b-row class="mt-2">
			<b-col md="2">
				<sidebar-vue />
			</b-col>
			<b-col md="10">
				<b-card title="Update Requests" class="">
					<b-table
						:items="data"
						:fields="fields"
						responsive="md"
						head-variant="info"
						class="mt-2"
					>
						<template #cell(index)="row">
							{{ row.index + 1 }}
						</template>
						<template #cell(actions)="row">
							<b-icon
								icon="check"
								v-b-tooltip.hover.top="'Approve'"
								font-scale="1.5"
								@click="action(row.item.id, 3)"
								role="button"
							/>
							<b-icon
								icon="x"
								v-b-tooltip.hover.top="'Disapprove'"
								font-scale="1.5"
								@click="action(row.item.id, 1)"
								role="button"
							/>
							<b-icon
								icon="eye"
								v-b-tooltip.hover.top="'View'"
								font-scale="1.5"
								@click="view(row.item.id)"
								role="button"
							/>
						</template>
					</b-table>
				</b-card>
			</b-col>
		</b-row>
	</div>
</template>
<script>
import HeaderVue from '@/components/header/Header.vue';
import SidebarVue from '@/components/sidebar/Sidebar.vue';
export default {
	name: 'RequestsView',
	components: {
		HeaderVue,
		SidebarVue,
	},
	data() {
		return {
			data: [],
			fields: [
				{ key: 'index', sortable: true },
				{ key: 'nin', sortable: true },
				{ key: 'full_name', sortable: true },
				{ key: 'email', sortable: true },
				{ key: 'occupation', sortable: true },
				{ key: 'phone', sortable: true },
				{ key: 'next_of_kin', sortable: true },
				{ key: 'actions', sortable: false },
			],
			items: [
				{
					isActive: true,
					nin: 40,
					first_name: 'Dickerson',
					last_name: 'Macdonald',
				},
				{ isActive: false, nin: 21, first_name: 'Larsen', last_name: 'Shaw' },
				{ isActive: false, nin: 89, first_name: 'Geneva', last_name: 'Wilson' },
				{ isActive: true, nin: 38, first_name: 'Jami', last_name: 'Carney' },
			],
		};
	},
	created() {
		this.getUpdateRequest();
	},
	methods: {
		async getUpdateRequest() {
			await this.axios
				.get(`api/update-request/`)
				.then(({ data }) => {
					this.data = data.map((obj) => ({
						id: obj.id,
						nin: obj.citizen.user.nin,
						full_name: `${obj.citizen.user.first_name} ${obj.citizen.user.last_name}`,
						email: obj.citizen.user.email,
						phone: obj.citizen.user.phone,
						occupation: obj.occupation,
						next_of_kin: obj.next_of_kin,
					}));
				})
				.catch((err) => {
					console.log(err);
				});
		},
		async action(id, status) {
			const data = { status: status };
			await this.axios
				.patch(`api/update-nininfo/${id}/`, data)
				.then(() => {
					this.getUpdateRequest();
				})
				.catch(() => {});
		},
	},
};
</script>
